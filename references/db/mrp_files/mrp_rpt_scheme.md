# 报表方案定义-mrp_rpt_scheme

## 仓库-多选基础资料表 t_mrp_rpt_scheme_store

- **表名称：** 仓库-多选基础资料表
- **表名：** t_mrp_rpt_scheme_store

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rpt_scheme_store |  | fpkid |
| 2 | idx_mrp_rpt_scheme_store |  | fentryid |

---

## 报表方案定义-使用范围位图表 t_mrp_rptscheme_m

- **表名称：** 报表方案定义-使用范围位图表
- **表名：** t_mrp_rptscheme_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rptscheme_m |  | forgid |

---

## 报表方案定义-多语言表 t_mrp_rptscheme_l

- **表名称：** 报表方案定义-多语言表
- **表名：** t_mrp_rptscheme_l

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
| 1 | pk_t_mrp_rptscheme_l |  | fpkid |
| 2 | idx_mrp_rptscheme_l |  | fid,flocaleid |

---

## 报表方案定义-使用范围表 t_mrp_rptscheme_u

- **表名称：** 报表方案定义-使用范围表
- **表名：** t_mrp_rptscheme_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rptscheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_mrp_rptscheme_u_uo |  | fuseorgid |

---

## MRP计划方案-多选基础资料表 t_mrp_rpt_scheme_plan

- **表名称：** MRP计划方案-多选基础资料表
- **表名：** t_mrp_rpt_scheme_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 计划方案 mrp_planscheme |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rpt_scheme_plan |  | fpkid |
| 2 | idx_mrp_rpt_scheme_plan |  | fid |

---

## 需求来源-多选基础资料表 t_mrp_rpt_scheme_source

- **表名称：** 需求来源-多选基础资料表
- **表名：** t_mrp_rpt_scheme_source

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_rpt_scheme_source |  | fid |
| 2 | pk_t_mrp_rpt_scheme_source |  | fpkid |

---

## 报表方案定义-主表 t_mrp_rptscheme

- **表名称：** 报表方案定义-主表
- **表名：** t_mrp_rptscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpassdate | 显示过去日期 | bpchar | 1 |  | √ | ' ' | 显示过去日期 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fstarttime | 起始日期 | varchar | 50 |  | √ | ' ' | 起始日期,枚举: A :报表创建日期 B :历史最早日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | frpttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: mrp_stock_forecast :备料预测 mrp_production_forecast :生产预测 mrp_documents_plan :交单计划 |
| 20 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_rptscheme |  | fnumber |
| 2 | idx_t_mrp_rptscheme_master |  | fmasterid |
| 3 | pk_t_mrp_rptscheme |  | fid |
| 4 | idx_t_mrp_rptscheme_createorg |  | fcreateorgid |

---

## 仓位-多选基础资料表 t_mrp_rpt_scheme_location

- **表名称：** 仓位-多选基础资料表
- **表名：** t_mrp_rpt_scheme_location

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rpt_scheme_location |  | fpkid |
| 2 | idx_mrp_rpt_scheme_lo |  | fentryid |

---

## 库存查询范围-子表 t_mrp_rpt_scheme_inv

- **表名称：** 库存查询范围-子表
- **表名：** t_mrp_rpt_scheme_inv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: inventory :库存 delivery :发货 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fordersource | 订单发货来源 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 6 | frptfield | 报表字段 | varchar | 50 |  | √ | ' ' | 报表字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_rpt_scheme_inv |  | fid |
| 2 | pk_t_mrp_rpt_scheme_inv |  | fentryid |

---

## 时间列-子表 t_mrp_rpt_scheme_time

- **表名称：** 时间列-子表
- **表名：** t_mrp_rpt_scheme_time

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fissumlast | 统计上一维度 | bpchar | 1 |  | √ | ' ' | 统计上一维度 |
| 3 | flength | 长度 | int4 | 32 |  | √ | 0 | 长度 |
| 4 | fdisplaydate | 显示日期 | varchar | 50 |  | √ | ' ' | 显示日期,枚举: Mon :周一 Tue :周二 Wed :周三 Thu :周四 Fri :周五 Sat :周六 Sun :周日 FirstDay :每月1号 |
| 5 | fissumlatest | 统计至最晚日期 | bpchar | 1 |  | √ | ' ' | 统计至最晚日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftimetype | 时间维度 | varchar | 50 |  | √ | ' ' | 时间维度,枚举: day :天 week :周 month :月 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_rpt_scheme_time |  | fid,fseq |
| 2 | pk_t_mrp_rpt_scheme_time |  | fentryid |
