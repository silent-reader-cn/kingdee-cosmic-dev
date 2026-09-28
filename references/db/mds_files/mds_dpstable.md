# dps报表基础资料-mds_dpstable

## 单据体-子表 t_mds_dpsweek

- **表名称：** 单据体-子表
- **表名：** t_mds_dpsweek

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuporg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmaterielweek | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fmbommaterial | mbom物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fweekplan | P_DPS周计划 | numeric | 23 | 10 | √ | 0 | P_DPS周计划 |
| 6 | fweekresult | P_DPS周结果 | numeric | 23 | 10 | √ | 0 | P_DPS周结果 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fweekdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fweekdemand | P_DPS周需求 | numeric | 23 | 10 | √ | 0 | P_DPS周需求 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dpsweek |  | fentryid |
| 2 | idx_mds_dpsweek_fid |  | fid |

---

## DPS排产物料编码-多选基础资料表 t_mds_dpsplanmaterial

- **表名称：** DPS排产物料编码-多选基础资料表
- **表名：** t_mds_dpsplanmaterial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dpsplanmaterial |  | fpkid |
| 2 | idx_mds_dpsplanmaterial_fid |  | fid |

---

## MBOM-多选基础资料表 t_mds_dpstablembom

- **表名称：** MBOM-多选基础资料表
- **表名：** t_mds_dpstablembom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_dpstablembom_fid |  | fid |
| 2 | pk_mds_dpstablembom |  | fpkid |

---

## DPS排产组织编码-多选基础资料表 t_mds_dpsplanmaterialorg

- **表名称：** DPS排产组织编码-多选基础资料表
- **表名：** t_mds_dpsplanmaterialorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dpsplanmaterialorg |  | fpkid |
| 2 | idx_mds_dpsplanmaterialorg_fid |  | fid |

---

## dps报表基础资料-主表 t_mds_dpstable

- **表名称：** dps报表基础资料-主表
- **表名：** t_mds_dpstable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpspartno | PSpart(S) | varchar | 50 |  | √ | ' ' | PSpart(S) |
| 3 | fsummaryfamily | 产品族 | varchar | 50 |  | √ | ' ' | 产品族 |
| 4 | fsummarycolor | 颜色 | varchar | 50 |  | √ | ' ' | 颜色 |
| 5 | fsummaryline | 产品线 | varchar | 50 |  | √ | ' ' | 产品线 |
| 6 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fmaterielmf | MF(MF组件) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | forgdpssite | DPS Site | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fdpssitename | Site名称 | varchar | 50 |  | √ | ' ' | Site名称 |
| 14 | fdpsarrangeset | DPS待排产定义 | int8 | 64 |  | √ | 0 | 日生产计划待排表定义 mds_dpsarrangeset |
| 15 | fmanumode | 制造模式 | varchar | 50 |  | √ | ' ' | 制造模式 |
| 16 | fisno | 是否服务编码 | bpchar | 1 |  | √ | '0' | 是否服务编码 |
| 17 | fsummarymodel | 产品型号 | varchar | 50 |  | √ | ' ' | 产品型号 |
| 18 | fdpssiteno | Site编码 | varchar | 50 |  | √ | ' ' | Site编码 |
| 19 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fppartm | Ppart(M) | varchar | 50 |  | √ | ' ' | Ppart(M) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fuser | 生产计划 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fmitem | ITEM | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 25 | fopenproductfamily | 是否开启产品族 | bpchar | 1 |  | √ | '0' | 是否开启产品族 |
| 26 | fpbom | PBOM | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 27 | fsummaryfield | 产品域 | varchar | 50 |  | √ | ' ' | 产品域 |
| 28 | flastupdatetime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 29 | fsummaryseries | 产品系列 | varchar | 50 |  | √ | ' ' | 产品系列 |
| 30 | fpsparttype | PSpart(S)类型 | varchar | 50 |  | √ | ' ' | PSpart(S)类型 |
| 31 | fsupportmode | 供应模式 | varchar | 50 |  | √ | ' ' | 供应模式 |
| 32 | fmaterieldps | P_DPS对象 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 33 | fenable | 使用状态 | varchar | 5 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 35 | fpspart | PSpart(S) | int8 | 64 |  | √ | 0 | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dpstable |  | fid |
| 2 | idx_mds_dpstable_number |  | fnumber |

---

## dps报表基础资料-分表 t_mds_dpstable_a

- **表名称：** dps报表基础资料-分表
- **表名：** t_mds_dpstable_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweekdelivery | 本周发货 | numeric | 23 | 10 | √ | 0 | 本周发货 |
| 3 | fmtwogap | M2GAP | numeric | 23 | 10 | √ | 0 | M2GAP |
| 4 | fweekresultgap | 周结果GAP | numeric | 23 | 10 | √ | 0 | 周结果GAP |
| 5 | fprestock | 预留库存 | numeric | 23 | 10 | √ | 0 | 预留库存 |
| 6 | fprocess | 在制 | numeric | 23 | 10 | √ | 0 | 在制 |
| 7 | fdemandsend | 待发需求 | numeric | 23 | 10 | √ | 0 | 待发需求 |
| 8 | fmtwopredisplace | M2预排量 | numeric | 23 | 10 | √ | 0 | M2预排量 |
| 9 | fweekplangap | 周计划GAP | numeric | 23 | 10 | √ | 0 | 周计划GAP |
| 10 | fmtwouse | M2未排量/用量 | numeric | 23 | 10 | √ | 0 | M2未排量/用量 |
| 11 | fmonegap | GAP | numeric | 23 | 10 | √ | 0 | GAP |
| 12 | fsafestock | 安全库存 | numeric | 23 | 10 | √ | 0 | 安全库存 |
| 13 | fbaremargin | 裸机余量/裸机用量 | numeric | 23 | 10 | √ | 0 | 裸机余量/裸机用量 |
| 14 | favastock | 可用库存 | numeric | 23 | 10 | √ | 0 | 可用库存 |
| 15 | fprofaulty | 故障品*比例 | numeric | 23 | 10 | √ | 0 | 故障品*比例 |
| 16 | fwaitdisplace | 待排量 | numeric | 23 | 10 | √ | 0 | 待排量 |
| 17 | fweekdelivered | 过去周已发货 | numeric | 23 | 10 | √ | 0 | 过去周已发货 |
| 18 | fmtwodemand | M2需求 | numeric | 23 | 10 | √ | 0 | M2需求 |
| 19 | fpredisplace | 预排量 | numeric | 23 | 10 | √ | 0 | 预排量 |
| 20 | fdisplacement | 已排量 | numeric | 23 | 10 | √ | 0 | 已排量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_dpstable_a_q |  | fweekdelivery |
| 2 | pk_mds_dpstable_a |  | fid |

---

## dps报表基础资料-多语言表 t_mds_dpstable_l

- **表名称：** dps报表基础资料-多语言表
- **表名：** t_mds_dpstable_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_dpstable_l |  | fpkid |
| 2 | idx_mds_dpstable_l |  | fid,flocaleid |
