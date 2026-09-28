# 折旧方法配置-fa_depremethod_conf

## 单据体-子表 t_fa_depremethod_conf_e

- **表名称：** 单据体-子表
- **表名：** t_fa_depremethod_conf_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaxcompare | 上限比较符 | varchar | 10 |  | √ | ' ' | 上限比较符,枚举: < :小于 <= :小于等于 |
| 3 | flimitcompare | 下限比较符 | varchar | 10 |  | √ | ' ' | 下限比较符,枚举: > :大于 >= :大于等于 |
| 4 | fdepreratio | 折旧系数 | numeric | 19 | 6 | √ | 0 | 折旧系数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fuseyearmax | 预计使用年限上限 | int4 | 32 |  | √ | 0 | 预计使用年限上限 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fuseyearlimit | 预计使用年限下限 | int4 | 32 |  | √ | 0 | 预计使用年限下限 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_depremethod_conf_e_fid |  | fid |
| 2 | pk_fa_depremethod_conf_e |  | fentryid |

---

## 折旧方法配置-主表 t_fa_depremethod_c

- **表名称：** 折旧方法配置-主表
- **表名：** t_fa_depremethod_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdepremethod | 折旧方法 | int8 | 64 |  | √ | 0 | [折旧方法 fa_depremethod](../fa_files/fa_depremethod.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depremethod_c |  | fdepremethod |
| 2 | pk_fa_depremethod_c |  | fid |
