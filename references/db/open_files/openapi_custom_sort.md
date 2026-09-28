# 自定义分类维护-openapi_custom_sort

## 自定义分类维护-主表 t_openapi_custom_sort

- **表名称：** 自定义分类维护-主表
- **表名：** t_openapi_custom_sort

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 分类描述 | varchar | 500 |  | √ | ' ' | 分类描述 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 分类名称 | varchar | 255 |  | √ | ' ' | 分类名称 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 分类编码 | varchar | 30 |  | √ | ' ' | 分类编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_custom_sort |  | fid |
| 2 | idx_t_open_cust_sort_fnumber |  | fnumber |

---

## 自定义分类维护-多语言表 t_openapi_custom_sort_l

- **表名称：** 自定义分类维护-多语言表
- **表名：** t_openapi_custom_sort_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 分类描述 | varchar | 500 |  | √ | ' ' | 分类描述 |
| 3 | fname | 分类名称 | varchar | 255 |  | √ | ' ' | 分类名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_open_cust_sort_l_fid |  | fid,flocaleid |
| 2 | pk_t_openapi_custom_sort_l |  | fpkid |
