# 取消组织职能校验-er_orgcheckconfig

## 校验字段-子表 t_er_bizorgcheckdetail

- **表名称：** 校验字段-子表
- **表名：** t_er_bizorgcheckdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentity | 单头/分录 | varchar | 100 |  | √ | ' ' | 单头/分录 |
| 3 | fkey | 字段 | varchar | 100 |  | √ | ' ' | 字段 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_bizorgck_entity |  | fentity,fseq |
| 2 | t_er_bizorgcheckdetail_pkey |  | fentryid |
| 3 | idx_er_bizorgck_key |  | fkey |

---

## 取消组织职能校验-主表 t_er_bizorgcheckconfig

- **表名称：** 取消组织职能校验-主表
- **表名：** t_er_bizorgcheckconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitytype | 单据类型 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | ffuntype | 职能类型 | varchar | 10 |  | √ | ' ' | 职能类型,枚举: 01 :行政管理 02 :采购职能 03 :销售职能 04 :生产职能 05 :库存管理 06 :质检职能 07 :结算职能 08 :资金管理 09 :资产管理 10 :核算主体 11 :共享中心 13 :预算职能 14 :控制单元 15 :业务单元 16 :主数据控制视图 12 :共享中心 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_bizorgcheckconfig_pkey |  | fid |
| 2 | idx_er_bizorgck_type |  | fentitytype |
