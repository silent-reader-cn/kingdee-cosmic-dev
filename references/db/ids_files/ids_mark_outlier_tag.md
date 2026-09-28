# 数据标签-ids_mark_outlier_tag

## 数据标签-多语言表 t_ids_mark_outlier_tag_l

- **表名称：** 数据标签-多语言表
- **表名：** t_ids_mark_outlier_tag_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 标签名称 | varchar | 100 |  | √ | ' ' | 标签名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_mark_outlier_tag_l |  | fpkid |
| 2 | idx_ids_tag_l_fid |  | fid |

---

## 数据标签-主表 t_ids_mark_outlier_tag

- **表名称：** 数据标签-主表
- **表名：** t_ids_mark_outlier_tag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :未启用 1 :已启用 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 标签名称 | varchar | 100 |  | √ | ' ' | 标签名称 |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftype | 标签类型 | varchar | 50 |  | √ | ' ' | 标签类型,枚举: finvorgid :库存组织标签 fwarehouseid :仓库标签 fcustid :客户标签 fmaterialid :物料标签 bill :单据标签 fother :其他 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fispreinsdata | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fnumber | 标签编码 | varchar | 80 |  | √ | ' ' | 标签编码 |
| 11 | fdescription | 标签说明 | varchar | 255 |  | √ | ' ' | 标签说明 |
| 12 | fallowtimeconfig | 是否支持配置影响时间范围 | bpchar | 1 |  | √ | '0' | 是否支持配置影响时间范围 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_mark_outlier_tag |  | fid |
| 2 | idx_ids_tag_number |  | fnumber |
