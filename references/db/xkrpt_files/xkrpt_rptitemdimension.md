# 项目维度数据-xkrpt_rptitemdimension

## 项目维度数据-主表 t_xkrpt_rptitemdimension

- **表名称：** 项目维度数据-主表
- **表名：** t_xkrpt_rptitemdimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | freportid | 报表id | varchar | 36 |  | √ | ' ' | 报表id |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fdimensionkey | 维度Key | text | 0 |  |  | null | 维度Key |
| 8 | fdimensionids | 维度ids | text | 0 |  |  | null | 维度ids |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_dimensionen_frptid |  | freportid |
| 2 | pk_t_xkrpt_rptitemdimension |  | fid |

---

## 单据体-子表 t_xkrpt_dimensionentry

- **表名称：** 单据体-子表
- **表名：** t_xkrpt_dimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensiondataid | 维度数据ID | int8 | 64 |  | √ | 0 | 维度数据ID |
| 3 | fdimensiondataname | 维度数据名称 | varchar | 250 |  | √ | ' ' | 维度数据名称 |
| 4 | fdimensionid | 维度ID | int8 | 64 |  | √ | 0 | 维度ID |
| 5 | fdimensionname | 维度名称 | varchar | 250 |  | √ | ' ' | 维度名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdimensionkey | dimensionKey | text | 0 |  |  | null | dimensionKey |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fdimensiondatanumber | 维度数据编码 | varchar | 250 |  | √ | ' ' | 维度数据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_dimensionentry_fid |  | fid |
| 2 | pk_t_xkrpt_dimensionentry |  | fentryid |
