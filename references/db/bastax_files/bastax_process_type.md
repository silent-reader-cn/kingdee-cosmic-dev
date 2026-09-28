# 自定义税要素类型-bastax_process_type

## 自定义税要素类型-主表 t_bastax_process_type

- **表名称：** 自定义税要素类型-主表
- **表名：** t_bastax_process_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fdatasource | 值来源废弃 | int8 | 64 |  | √ | 0 | 数据源配置 tctb_custom_datasource |
| 9 | fdatasourcevar | 值来源 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fprocesstype | 值类型 | varchar | 50 |  | √ | ' ' | 值类型,枚举: 0 :基础资料 1 :文本 2 :数值 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_process_type |  | fid |
| 2 | idx_bastax_process_type |  | fnumber |

---

## 自定义税要素类型-多语言表 t_bastax_process_type_l

- **表名称：** 自定义税要素类型-多语言表
- **表名：** t_bastax_process_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_process_type_l |  | fpkid |
| 2 | idx_bastax_process_type_l_0 |  | fid,flocaleid |
