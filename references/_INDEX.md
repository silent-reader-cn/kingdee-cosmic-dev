# 金蝶云苍穹开发知识库 · 总索引

本知识库由两大块构成，**全部内容可用同一个检索脚本定位**：

| 块 | 内容 | 规模 | 入口 |
| :--- | :--- | :--- | :--- |
| **块一 数据库** | 全量物理表结构（字段/列规则/索引） | 22769 张表 / 224 模块 | [db/_INDEX.md](./db/_INDEX.md) |
| **块二 OpenAPI 手册** | 金蝶云社区开放平台官方手册 | 144 篇 / 8 分类 | [openapi/_INDEX.md](./openapi/_INDEX.md) |

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。

## 检索

```bash
python scripts/search.py 销售订单                            # 全库检索
python scripts/search.py t_sm_salorder --table --full        # 精确取表字段
python scripts/search.py 自定义API --scope openapi           # 只搜开发手册
python scripts/search.py 回调 --scope openapi --category 开放事件
python scripts/search.py --list                              # 列出模块与分类
```

## 块一 数据库 · 模块概览

| 序号 | 模块 | 表数量 | 模块索引 |
| :---: | :--- | ---: | :--- |
| 1 | `src` | 1400 | [src_files/_INDEX.md](./db/src_files/_INDEX.md) |
| 2 | `em` | 675 | [em_files/_INDEX.md](./db/em_files/_INDEX.md) |
| 3 | `base` | 624 | [base_files/_INDEX.md](./db/base_files/_INDEX.md) |
| 4 | `mpdm` | 618 | [mpdm_files/_INDEX.md](./db/mpdm_files/_INDEX.md) |
| 5 | `srm` | 606 | [srm_files/_INDEX.md](./db/srm_files/_INDEX.md) |
| 6 | `im` | 587 | [im_files/_INDEX.md](./db/im_files/_INDEX.md) |
| 7 | `iscb` | 482 | [iscb_files/_INDEX.md](./db/iscb_files/_INDEX.md) |
| 8 | `tccit` | 419 | [tccit_files/_INDEX.md](./db/tccit_files/_INDEX.md) |
| 9 | `pbd` | 408 | [pbd_files/_INDEX.md](./db/pbd_files/_INDEX.md) |
| 10 | `tcvat` | 407 | [tcvat_files/_INDEX.md](./db/tcvat_files/_INDEX.md) |
| 11 | `plmsm` | 397 | [plmsm_files/_INDEX.md](./db/plmsm_files/_INDEX.md) |
| 12 | `basedata` | 362 | [basedata_files/_INDEX.md](./db/basedata_files/_INDEX.md) |
| 13 | `fmm` | 358 | [fmm_files/_INDEX.md](./db/fmm_files/_INDEX.md) |
| 14 | `sfc` | 321 | [sfc_files/_INDEX.md](./db/sfc_files/_INDEX.md) |
| 15 | `fa` | 313 | [fa_files/_INDEX.md](./db/fa_files/_INDEX.md) |
| 16 | `sco` | 302 | [sco_files/_INDEX.md](./db/sco_files/_INDEX.md) |
| 17 | `cas` | 300 | [cas_files/_INDEX.md](./db/cas_files/_INDEX.md) |
| 18 | `cal` | 290 | [cal_files/_INDEX.md](./db/cal_files/_INDEX.md) |
| 19 | `wf` | 279 | [wf_files/_INDEX.md](./db/wf_files/_INDEX.md) |
| 20 | `gl` | 259 | [gl_files/_INDEX.md](./db/gl_files/_INDEX.md) |
| 21 | `qcbd` | 256 | [qcbd_files/_INDEX.md](./db/qcbd_files/_INDEX.md) |
| 22 | `mds` | 254 | [mds_files/_INDEX.md](./db/mds_files/_INDEX.md) |
| 23 | `tdm` | 251 | [tdm_files/_INDEX.md](./db/tdm_files/_INDEX.md) |
| 24 | `msplan` | 244 | [msplan_files/_INDEX.md](./db/msplan_files/_INDEX.md) |
| 25 | `scp` | 242 | [scp_files/_INDEX.md](./db/scp_files/_INDEX.md) |
| 26 | `ar` | 239 | [ar_files/_INDEX.md](./db/ar_files/_INDEX.md) |
| 27 | `ifm` | 238 | [ifm_files/_INDEX.md](./db/ifm_files/_INDEX.md) |
| 28 | `ssc` | 221 | [ssc_files/_INDEX.md](./db/ssc_files/_INDEX.md) |
| 29 | `plmpm` | 219 | [plmpm_files/_INDEX.md](./db/plmpm_files/_INDEX.md) |
| 30 | `pds` | 217 | [pds_files/_INDEX.md](./db/pds_files/_INDEX.md) |
| 31 | `cts` | 207 | [cts_files/_INDEX.md](./db/cts_files/_INDEX.md) |
| 32 | `pom` | 207 | [pom_files/_INDEX.md](./db/pom_files/_INDEX.md) |
| 33 | `adm` | 205 | [adm_files/_INDEX.md](./db/adm_files/_INDEX.md) |
| 34 | `ocdbd` | 204 | [ocdbd_files/_INDEX.md](./db/ocdbd_files/_INDEX.md) |
| 35 | `mpm` | 200 | [mpm_files/_INDEX.md](./db/mpm_files/_INDEX.md) |
| 36 | `ap` | 199 | [ap_files/_INDEX.md](./db/ap_files/_INDEX.md) |
| 37 | `sm` | 190 | [sm_files/_INDEX.md](./db/sm_files/_INDEX.md) |
| 38 | `mrp` | 189 | [mrp_files/_INDEX.md](./db/mrp_files/_INDEX.md) |
| 39 | `tcret` | 183 | [tcret_files/_INDEX.md](./db/tcret_files/_INDEX.md) |
| 40 | `xkbm` | 181 | [xkbm_files/_INDEX.md](./db/xkbm_files/_INDEX.md) |
| … | 其余 184 个模块 | | 见 [db/_INDEX.md](./db/_INDEX.md) |

## 块二 OpenAPI 手册 · 分类概览

| 序号 | 一级分类 | 篇数 |
| :---: | :--- | ---: |
| 1 | [用户手册](./openapi/_INDEX.md#用户手册) | 81 |
| 2 | [常见问题](./openapi/_INDEX.md#常见问题) | 35 |
| 3 | [动态与公告](./openapi/_INDEX.md#动态与公告) | 11 |
| 4 | [开放事件](./openapi/_INDEX.md#开放事件) | 7 |
| 5 | [优秀实践](./openapi/_INDEX.md#优秀实践) | 5 |
| 6 | [接口规范](./openapi/_INDEX.md#接口规范) | 2 |
| 7 | [新手指引](./openapi/_INDEX.md#新手指引) | 2 |
| 8 | [整体介绍](./openapi/_INDEX.md#整体介绍) | 1 |
