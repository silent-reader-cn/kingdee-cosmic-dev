# 账户信息-er_busicardinfo

## 账户信息-多语言表 t_er_busicardinfo_l

- **表名称：** 账户信息-多语言表
- **表名：** t_er_busicardinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_busicardinfo_fid |  | fid |
| 2 | pk_t_er_busicardinfo_l |  | fpkid |

---

## 账户信息-主表 t_er_busicardinfo

- **表名称：** 账户信息-主表
- **表名：** t_er_busicardinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fuser | 员工 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcirculationflag | 流通状态 | varchar | 50 |  | √ | ' ' | 流通状态,枚举: Y :不流通 N :流通 |
| 6 | fdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | faccout | 银行账户 | varchar | 50 |  | √ | ' ' | 银行账户 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fserver | 服务商 | int8 | 64 |  | √ | 0 | 服务商设置 er_biz_info |
| 13 | fcanceldate | 销卡日期 | timestamp | 0 |  |  | null | 销卡日期 |
| 14 | factivationdate | 开卡日期 | timestamp | 0 |  |  | null | 开卡日期 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | factivationcode | 开卡标识 | varchar | 50 |  | √ | ' ' | 开卡标识 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fcardnumber | 银行卡号 | varchar | 50 |  | √ | ' ' | 银行卡号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fuer |  | fuser |
| 2 | idx_server |  | fserver |
| 3 | pk_t_er_busicardinfo |  | fid |
