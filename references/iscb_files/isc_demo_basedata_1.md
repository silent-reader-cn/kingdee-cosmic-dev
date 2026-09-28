# 基础资料demo1-isc_demo_basedata_1

## 基础资料demo1-主表 t_isc_demo_basedata_1

- **表名称：** 基础资料demo1-主表
- **表名：** t_isc_demo_basedata_1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fitemclass | 多类别基础资料 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 8 | fitemclasstype | 多类别基础资料类型 | varchar | 100 |  | √ | ' ' | 多类别基础资料类型,枚举: isc_data_copy :数据集成方案 isc_data_copy_trigger :启动方案 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_1_pkey |  | fid |
| 2 | idx_isc_demo_base_1 |  | fnumber |

---

## 基础资料demo1-多语言表 t_isc_demo_basedata_1_l

- **表名称：** 基础资料demo1-多语言表
- **表名：** t_isc_demo_basedata_1_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | falias_name | 别名 | varchar | 100 |  | √ | ' ' | 别名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_1_l_pkey |  | fpkid |
| 2 | idx_isc_demo_base_1_l |  | fid,flocaleid |

---

## 单据体-子表 t_isc_demo_basedata_e1

- **表名称：** 单据体-子表
- **表名：** t_isc_demo_basedata_e1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsex | 性别 | bpchar | 1 |  | √ | ' ' | 性别 |
| 3 | fbirthday | 出生时间 | timestamp | 0 |  |  | null | 出生时间 |
| 4 | fuser | 用户 | varchar | 100 |  | √ | ' ' | 用户 |
| 5 | fage | 年龄 | int8 | 64 |  | √ | 0 | 年龄 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fheight | 身高（m） | numeric | 23 | 10 | √ | 0.0000000000 | 身高（m） |
| 8 | fpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo_basedata_e1_pkey |  | fentryid |
| 2 | idx_isc_demo_base_e1 |  | fid |

---

## 附件-附件表 t_isc_demo1_file

- **表名称：** 附件-附件表
- **表名：** t_isc_demo1_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_demo1_file_pkey |  | fpkid |
| 2 | idx_isc_demo1_file_1 |  | fid |
