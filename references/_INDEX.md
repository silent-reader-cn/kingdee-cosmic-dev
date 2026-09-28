# 金蝶云苍穹开发知识库 · 总索引

本知识库由两大块构成，**全部内容可用同一个检索脚本定位**：

| 块 | 内容 | 规模 | 入口 |
| :--- | :--- | :--- | :--- |
| **块一 数据库** | 全量物理表结构（字段/列规则/索引） | 31547 张表 / 267 模块 | [db/_INDEX.md](./db/_INDEX.md) |
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
| 1 | `src` | 2144 | [src_files/_INDEX.md](./db/src_files/_INDEX.md) |
| 2 | `plmsm` | 979 | [plmsm_files/_INDEX.md](./db/plmsm_files/_INDEX.md) |
| 3 | `em` | 815 | [em_files/_INDEX.md](./db/em_files/_INDEX.md) |
| 4 | `srm` | 742 | [srm_files/_INDEX.md](./db/srm_files/_INDEX.md) |
| 5 | `mpdm` | 704 | [mpdm_files/_INDEX.md](./db/mpdm_files/_INDEX.md) |
| 6 | `base` | 680 | [base_files/_INDEX.md](./db/base_files/_INDEX.md) |
| 7 | `im` | 680 | [im_files/_INDEX.md](./db/im_files/_INDEX.md) |
| 8 | `pbd` | 525 | [pbd_files/_INDEX.md](./db/pbd_files/_INDEX.md) |
| 9 | `iscb` | 493 | [iscb_files/_INDEX.md](./db/iscb_files/_INDEX.md) |
| 10 | `tcvat` | 463 | [tcvat_files/_INDEX.md](./db/tcvat_files/_INDEX.md) |
| 11 | `tccit` | 458 | [tccit_files/_INDEX.md](./db/tccit_files/_INDEX.md) |
| 12 | `basedata` | 428 | [basedata_files/_INDEX.md](./db/basedata_files/_INDEX.md) |
| 13 | `pur` | 368 | [pur_files/_INDEX.md](./db/pur_files/_INDEX.md) |
| 14 | `fa` | 360 | [fa_files/_INDEX.md](./db/fa_files/_INDEX.md) |
| 15 | `sfc` | 359 | [sfc_files/_INDEX.md](./db/sfc_files/_INDEX.md) |
| 16 | `fmm` | 358 | [fmm_files/_INDEX.md](./db/fmm_files/_INDEX.md) |
| 17 | `mpm` | 350 | [mpm_files/_INDEX.md](./db/mpm_files/_INDEX.md) |
| 18 | `plmpm` | 342 | [plmpm_files/_INDEX.md](./db/plmpm_files/_INDEX.md) |
| 19 | `cal` | 332 | [cal_files/_INDEX.md](./db/cal_files/_INDEX.md) |
| 20 | `plmrm` | 328 | [plmrm_files/_INDEX.md](./db/plmrm_files/_INDEX.md) |
| 21 | `pmm` | 325 | [pmm_files/_INDEX.md](./db/pmm_files/_INDEX.md) |
| 22 | `xkbm` | 319 | [xkbm_files/_INDEX.md](./db/xkbm_files/_INDEX.md) |
| 23 | `cas` | 317 | [cas_files/_INDEX.md](./db/cas_files/_INDEX.md) |
| 24 | `sco` | 312 | [sco_files/_INDEX.md](./db/sco_files/_INDEX.md) |
| 25 | `scp` | 301 | [scp_files/_INDEX.md](./db/scp_files/_INDEX.md) |
| 26 | `gl` | 289 | [gl_files/_INDEX.md](./db/gl_files/_INDEX.md) |
| 27 | `wf` | 289 | [wf_files/_INDEX.md](./db/wf_files/_INDEX.md) |
| 28 | `qcbd` | 283 | [qcbd_files/_INDEX.md](./db/qcbd_files/_INDEX.md) |
| 29 | `cts` | 276 | [cts_files/_INDEX.md](./db/cts_files/_INDEX.md) |
| 30 | `tdm` | 272 | [tdm_files/_INDEX.md](./db/tdm_files/_INDEX.md) |
| 31 | `cfm` | 271 | [cfm_files/_INDEX.md](./db/cfm_files/_INDEX.md) |
| 32 | `pds` | 270 | [pds_files/_INDEX.md](./db/pds_files/_INDEX.md) |
| 33 | `mds` | 269 | [mds_files/_INDEX.md](./db/mds_files/_INDEX.md) |
| 34 | `ar` | 262 | [ar_files/_INDEX.md](./db/ar_files/_INDEX.md) |
| 35 | `adm` | 261 | [adm_files/_INDEX.md](./db/adm_files/_INDEX.md) |
| 36 | `ocdbd` | 254 | [ocdbd_files/_INDEX.md](./db/ocdbd_files/_INDEX.md) |
| 37 | `msplan` | 250 | [msplan_files/_INDEX.md](./db/msplan_files/_INDEX.md) |
| 38 | `sm` | 239 | [sm_files/_INDEX.md](./db/sm_files/_INDEX.md) |
| 39 | `mrp` | 235 | [mrp_files/_INDEX.md](./db/mrp_files/_INDEX.md) |
| 40 | `tcret` | 229 | [tcret_files/_INDEX.md](./db/tcret_files/_INDEX.md) |
| … | 其余 227 个模块 | | 见 [db/_INDEX.md](./db/_INDEX.md) |

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
