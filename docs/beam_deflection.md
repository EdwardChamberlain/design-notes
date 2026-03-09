# Beam Deflection

## Beam Deflection Formula

| Load case | Diagram | Maximum beam deflection |
|---|---|---|
| Cantilever with point load at free end | ![Cantilever with point load at free end](./assets/images/line_drawings/cantilever_point_load_end_2_clean_dark_mode.png) | $\delta_{\max} = \dfrac{PL^3}{3EI}$ |
| Cantilever with point load at distance \(a\) from the fixed end | ![Cantilever with point load at distance \(a\) from the fixed end](./assets/images/line_drawings/cantilever_point_load_offset_2_clean_dark_mode.png) | $\delta_{\max} = \dfrac{Pa^2(3L-a)}{6EI}$ |
| Cantilever with uniformly distributed load | ![Cantilever with uniformly distributed load](./assets/images/line_drawings/cantilever_udl_2_clean_dark_mode.png) | $\delta_{\max} = \dfrac{wL^4}{8EI}$ |
| Cantilever with triangular load, maximum at fixed end | ![Cantilever with triangular load, maximum at fixed end](./assets/images/line_drawings/cantilever_triangular_fixed_end_2_clean_dark_mode.png) | $\delta_{\max} = \dfrac{wL^4}{30EI}$ |
| Cantilever with triangular load, maximum at free end | ![Cantilever with triangular load, maximum at free end](./assets/images/line_drawings/cantilever_triangular_free_end_2_clean_dark_mode.png) | $\delta_{\max} = \dfrac{11wL^4}{120EI}$ |
| Cantilever with applied end moment | ![Cantilever with applied end moment](./assets/images/line_drawings/cantilever_end_moment_2_clean_dark_mode.png) | $\delta_{\max} = \dfrac{ML^2}{2EI}$ |

> OmniCalculator

Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.

## Second Moment of Area

<!-- table-class: table-layout-auto table-width-full -->
| Geometry | Diagram | Formula / Formulas |
|---|---|---|
| Rectangle | ![](./assets/images/line_drawings/rectangle_section_dark_mode.png) | $I_y = \dfrac{w h^3}{12}$<br>$I_z = \dfrac{h w^3}{12}$ |
| Circular hollow section | ![](./assets/images/line_drawings/annulus_section_dark_mode.png) | $I_y = \dfrac{(D^4 - d^4)\cdot \pi}{64}$<br>$I_z = \dfrac{(D^4 - d^4)\cdot \pi}{64}$ |
| I-section | ![](./assets/images/line_drawings/i_section_dark_mode.png) | $I_y = \dfrac{w h^3}{12} - \dfrac{(w - t_w)\cdot (h - 2t_w)^3}{12}$<br>$I_z = \dfrac{h w^3}{12} - \dfrac{(w - t_w)^3 \cdot (h - 2t_w)}{12}$ |
| Rectangular hollow section | ![](./assets/images/line_drawings/rhs_section_dark_mode.png) | $I_y = \dfrac{W H^3 - w h^3}{12}$<br>$I_z = \dfrac{H W^3 - h w^3}{12}$ |
| Circle | ![](./assets/images/line_drawings/circle_section_dark_mode.png) | $I_y = \dfrac{\pi D^4}{64}$<br>$I_z = \dfrac{\pi D^4}{64}$ |

> structuralbasics.com
