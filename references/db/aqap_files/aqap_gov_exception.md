# 异常分类管理-aqap_gov_exception

## 异常分类管理-多语言表 t_aqap_gov_exception_l

- **表名称：** 异常分类管理-多语言表
- **表名：** t_aqap_gov_exception_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_gov_exception_l |  | fpkid |
| 2 | idx_aqap_gov_exception_l_0 |  | fid,flocaleid |
| 3 | idx_cluster_gov_exception_l |  | fname |

---

## 异常分类管理-主表 t_aqap_gov_exception

- **表名称：** 异常分类管理-主表
- **表名：** t_aqap_gov_exception

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbd_exp | 异常类型 | int8 | 64 |  | √ | 0 | [异常类型 aqap_exception_type](../aqap_files/aqap_exception_type.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fvalue | 匹配特征值 | varchar | 255 |  | √ | ' ' | 匹配特征值 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fbd_biz_type | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 aqap_business_type](../aqap_files/aqap_business_type.md) |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fpattern | 提示语模板 | varchar | 500 |  | √ | ' ' | 提示语模板 |
| 14 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 15 | fdesc | 描述信息 | varchar | 255 |  | √ | ' ' | 描述信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_gov_exception |  | fid |
| 2 | index_cluster |  | fnumber |
