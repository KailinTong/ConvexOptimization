import numpy as np
import imageio
import matplotlib.pyplot as plt
import finite_differences as fd


def energy_primal(u):
    # TODO: implement
    return 0


def energy_dual(p):
    # TODO: implement
    return 0


def pgm():
    p = np.zeros((2 * m * n * c,))
    ep = np.zeros((num_iter,))
    ed = np.zeros((num_iter,))
    for i in range(num_iter):
        ep[i] = energy_primal(u_0 - D.T @ p)
        ed[i] = energy_dual(p)
        if i % 10 == 0:
            print(f'{i:4d}: energy={ed[i]:.3f}')

        # TODO: Derive/Implement

    u_ = (u_0 - D.T @ p).reshape(c, m, n).transpose(1, 2, 0)
    return u_, ep, ed


def fista():
    p = np.zeros((2 * m * n * c,))
    p_old = p.copy()
    t = 0
    ep = np.zeros((num_iter,))
    ed = np.zeros((num_iter,))
    for i in range(num_iter):
        ep[i] = energy_primal(u_0 - D.T @ p)
        ed[i] = energy_dual(p)
        if i % 10 == 0:
            print(f'{i:4d}: energy={ed[i]:.3f}')

        # TODO: Derive/Implement

    u_ = (u_0 - D.T @ p).reshape(c, m, n).transpose(1, 2, 0)
    return u_, ep, ed


def visualize(
    u_0,
    u_pgm, ep_pgm, ed_pgm,
    u_fista, ep_fista, ed_fista,
):
    fig, ax = plt.subplots(2, 2)

    ax[0, 0].imshow(u_0)
    ax[0, 1].imshow(target)
    ax[1, 0].imshow(u_pgm)
    ax[1, 1].imshow(u_fista)

    fig, ax = plt.subplots(1, 2)
    ax[0].loglog(ep_pgm, label='PGM')
    ax[0].loglog(ep_fista, label='FISTA')
    ax[0].grid()
    ax[0].legend()
    ax[1].loglog(ed_pgm, label='PGM')
    ax[1].loglog(ed_fista, label='FISTA')
    ax[1].grid()
    ax[1].legend()

    # TODO: visualize the primal-dual gap

    plt.show()


if __name__ == '__main__':
    target = imageio.imread('mars.png') / 255.
    m, n, c = target.shape
    u_0 = target + 0.2 * np.random.randn(*target.shape)
    # Construction of D assumes channels first
    u_0 = u_0.transpose(2, 0, 1).ravel()
    D = fd.D(m, n, c)
    L = 8

    lamda = 0.2
    num_iter = 400
    u_pgm, ep_pgm, ed_pgm = pgm()
    u_fista, ep_fista, ed_fista = fista()
    visualize(
        u_0.reshape(c, m, n).transpose(1, 2, 0),
        u_pgm, ep_pgm, ed_pgm,
        u_fista, ep_fista, ed_fista
    )