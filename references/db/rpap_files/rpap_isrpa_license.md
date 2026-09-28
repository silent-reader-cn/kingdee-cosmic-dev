# 许可-rpap_isrpa_license

## 许可-主表 t_rpap_isrpa_license

- **表名称：** 许可-主表
- **表名：** t_rpap_isrpa_license

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | flicenseenddate | 许可到期时间 | timestamp | 0 |  |  | null | 许可到期时间 |
| 5 | fdecount | 设计器许可总数 | int8 | 64 |  | √ | 0 | 设计器许可总数 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | flicensetype | 许可类型 | varchar | 30 |  | √ | ' ' | 许可类型 |
| 11 | flicensecreatedate | 许可导入时间 | timestamp | 0 |  |  | null | 许可导入时间 |
| 12 | fusedrbcount | 已使用机器人许可 | int8 | 64 |  | √ | 0 | 已使用机器人许可 |
| 13 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | frbcount | 机器人许可总数 | int8 | 64 |  | √ | 0 | 机器人许可总数 |
| 15 | flicensestate | 许可有效状态 | varchar | 30 |  | √ | ' ' | 许可有效状态,枚举: 1 :无效 0 :正常 3 :过期 |
| 16 | fnumber | 许可编码 | varchar | 255 |  | √ | ' ' | 许可编码 |
| 17 | fuseddecount | 已使用设计器许可 | int8 | 64 |  | √ | 0 | 已使用设计器许可 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isrpa_license_number |  | fnumber |
| 2 | pk_t_rpap_isrpa_license |  | fid |

---

## 许可-多语言表 t_rpap_isrpa_license_l

- **表名称：** 许可-多语言表
- **表名：** t_rpap_isrpa_license_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 许可名称 | varchar | 255 |  |  | ' ' | 许可名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isrpa_license_l_fid |  | fid |
| 2 | pk_t_rpap_isrpa_license_l |  | fpkid |
