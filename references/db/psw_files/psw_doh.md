# 预计可用天数-psw_doh

## 预计可用天数-主表 t_psw_doh

- **表名称：** 预计可用天数-主表
- **表名：** t_psw_doh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_doh |  | fid |
| 2 | idx_t_psw_doh |  | fbillno,fid |

---

## 预计可用天数明细-子表 t_psw_dohdetail

- **表名称：** 预计可用天数明细-子表
- **表名：** t_psw_dohdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdaysonhand60 |  | int4 | 32 |  | √ | 0 |  |
| 3 | fdaysonhand26 |  | int4 | 32 |  | √ | 0 |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdaysonhand25 |  | int4 | 32 |  | √ | 0 |  |
| 6 | fdaysonhand24 |  | int4 | 32 |  | √ | 0 |  |
| 7 | fdaysonhand23 |  | int4 | 32 |  | √ | 0 |  |
| 8 | fdaysonhand22 |  | int4 | 32 |  | √ | 0 |  |
| 9 | fdaysonhand21 |  | int4 | 32 |  | √ | 0 |  |
| 10 | fdaysonhand20 |  | int4 | 32 |  | √ | 0 |  |
| 11 | fsafetystock | 安全库存 | numeric | 23 | 10 | √ | 0 | 安全库存 |
| 12 | fdaysonhand29 |  | int4 | 32 |  | √ | 0 |  |
| 13 | fdaysonhand28 |  | int4 | 32 |  | √ | 0 |  |
| 14 | fdaysonhand27 |  | int4 | 32 |  | √ | 0 |  |
| 15 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fdaysonhand2 |  | int4 | 32 |  | √ | 0 |  |
| 18 | fdaysonhand1 |  | int4 | 32 |  | √ | 0 |  |
| 19 | fdaysonhand4 |  | int4 | 32 |  | √ | 0 |  |
| 20 | fdaysonhand37 |  | int4 | 32 |  | √ | 0 |  |
| 21 | fdaysonhand3 |  | int4 | 32 |  | √ | 0 |  |
| 22 | fdaysonhand36 |  | int4 | 32 |  | √ | 0 |  |
| 23 | fdaysonhand6 |  | int4 | 32 |  | √ | 0 |  |
| 24 | fdaysonhand35 |  | int4 | 32 |  | √ | 0 |  |
| 25 | fdaysonhand5 |  | int4 | 32 |  | √ | 0 |  |
| 26 | fdaysonhand34 |  | int4 | 32 |  | √ | 0 |  |
| 27 | fdaysonhand8 |  | int4 | 32 |  | √ | 0 |  |
| 28 | fdaysonhand33 |  | int4 | 32 |  | √ | 0 |  |
| 29 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fdaysonhand7 |  | int4 | 32 |  | √ | 0 |  |
| 31 | fdaysonhand32 |  | int4 | 32 |  | √ | 0 |  |
| 32 | fdaysonhand31 |  | int4 | 32 |  | √ | 0 |  |
| 33 | fdaysonhand9 |  | int4 | 32 |  | √ | 0 |  |
| 34 | fdaysonhand30 |  | int4 | 32 |  | √ | 0 |  |
| 35 | fdaysonhand39 |  | int4 | 32 |  | √ | 0 |  |
| 36 | fdaysonhand38 |  | int4 | 32 |  | √ | 0 |  |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fdaysonhand40 |  | int4 | 32 |  | √ | 0 |  |
| 39 | fdaysonhand48 |  | int4 | 32 |  | √ | 0 |  |
| 40 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 41 | fdaysonhand47 |  | int4 | 32 |  | √ | 0 |  |
| 42 | fdaysonhand46 |  | int4 | 32 |  | √ | 0 |  |
| 43 | fdaysonhand45 |  | int4 | 32 |  | √ | 0 |  |
| 44 | fdaysonhand44 |  | int4 | 32 |  | √ | 0 |  |
| 45 | fdaysonhand43 |  | int4 | 32 |  | √ | 0 |  |
| 46 | fdaysonhand42 |  | int4 | 32 |  | √ | 0 |  |
| 47 | fdaysonhand41 |  | int4 | 32 |  | √ | 0 |  |
| 48 | fdaysonhand49 |  | int4 | 32 |  | √ | 0 |  |
| 49 | fdaysonhand51 |  | int4 | 32 |  | √ | 0 |  |
| 50 | fdaysonhand50 |  | int4 | 32 |  | √ | 0 |  |
| 51 | fdaysonhand15 |  | int4 | 32 |  | √ | 0 |  |
| 52 | fdaysonhand59 |  | int4 | 32 |  | √ | 0 |  |
| 53 | fdaysonhand14 |  | int4 | 32 |  | √ | 0 |  |
| 54 | fdaysonhand58 |  | int4 | 32 |  | √ | 0 |  |
| 55 | fdaysonhand13 |  | int4 | 32 |  | √ | 0 |  |
| 56 | fdaysonhand57 |  | int4 | 32 |  | √ | 0 |  |
| 57 | fauxprop | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 58 | fdaysonhand12 |  | int4 | 32 |  | √ | 0 |  |
| 59 | fdaysonhand56 |  | int4 | 32 |  | √ | 0 |  |
| 60 | fdaysonhand11 |  | int4 | 32 |  | √ | 0 |  |
| 61 | fdaysonhand55 |  | int4 | 32 |  | √ | 0 |  |
| 62 | fdaysonhand10 |  | int4 | 32 |  | √ | 0 |  |
| 63 | fdaysonhand54 |  | int4 | 32 |  | √ | 0 |  |
| 64 | fdaysonhand53 |  | int4 | 32 |  | √ | 0 |  |
| 65 | fdaysonhand52 |  | int4 | 32 |  | √ | 0 |  |
| 66 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 67 | fdaysonhand19 |  | int4 | 32 |  | √ | 0 |  |
| 68 | fdaysonhand18 |  | int4 | 32 |  | √ | 0 |  |
| 69 | fdaysonhand17 |  | int4 | 32 |  | √ | 0 |  |
| 70 | fdaysonhand16 |  | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_dohdetail |  | fentryid |
| 2 | idx_t_psw_dohdetail |  | fmaterial,fentryid |
