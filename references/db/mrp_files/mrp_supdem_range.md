# 供需范围设置-mrp_supdem_range

## 供应-子表 t_mrp_supdem_sup

- **表名称：** 供应-子表
- **表名：** t_mrp_supdem_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsupplyconfig | 数据源配置 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconfig |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_supdem_sup |  | fid,fseq |
| 2 | pk_mrp_supdem_sup |  | fentryid |

---

## 供需范围设置-主表 t_mrp_supdem_range

- **表名称：** 供需范围设置-主表
- **表名：** t_mrp_supdem_range

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_supdem_range |  | fid |

---

## 需求-子表 t_mrp_supdem_dem

- **表名称：** 需求-子表
- **表名：** t_mrp_supdem_dem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdemandconfig | 数据源配置 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconfig |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_supdem_dem |  | fid,fseq |
| 2 | pk_mrp_supdem_dem |  | fentryid |
