# 信用申诉单-fircm_creditappeal

## 信用申诉单-多语言表 t_fircm_creditappeal_l

- **表名称：** 信用申诉单-多语言表
- **表名：** t_fircm_creditappeal_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fposition | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fircm_creditappeall_locale |  | flocaleid |
| 2 | pk_t_fircm_creditappeal_l |  | fpkid |

---

## 信用申诉单-主表 t_fircm_creditappeal

- **表名称：** 信用申诉单-主表
- **表名：** t_fircm_creditappeal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :申诉中 C :申诉通过 D :申诉不通过 |
| 4 | fcreatetime | 申诉日期 | timestamp | 0 |  |  | null | 申诉日期 |
| 5 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreditmodifylogid | 关联信用变更日志id | int8 | 64 |  | √ | 0 | 关联信用变更日志id |
| 7 | fcompany | 申诉人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fauditscore | 核定信用加分 | numeric | 19 | 6 | √ | 0 | 核定信用加分 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fappealreason | 申诉理由 | varchar | 1000 |  | √ | ' ' | 申诉理由 |
| 13 | fnextauditor | 当前处理人 | varchar | 50 |  | √ | ' ' | 当前处理人 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fappealscore | 申诉信用加分 | numeric | 19 | 6 | √ | 0 | 申诉信用加分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fircm_credit_appeal |  | fbillno |
| 2 | pk_t_fircm_creditappeal |  | fid |
