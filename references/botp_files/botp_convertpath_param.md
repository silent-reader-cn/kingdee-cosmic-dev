# 转换路线参数-botp_convertpath_param

## 转换路线参数-主表 t_botp_convertpath_param

- **表名称：** 转换路线参数-主表
- **表名：** t_botp_convertpath_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftargetbillnumber | 目标单标识 | varchar | 50 |  | √ | ' ' | 目标单标识 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fenablecarrycreaterule | 开启新建规则携带 | bpchar | 1 |  | √ | '0' | 开启新建规则携带 |
| 7 | fmustinput_tag | 必录控制_详情 | text | 0 |  |  | null | 必录控制_详情 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fsourcebillnumber | 源单标识 | varchar | 50 |  | √ | ' ' | 源单标识 |
| 11 | fdisablecreaterule | 禁止新建规则 | bpchar | 1 |  | √ | '0' | 禁止新建规则 |
| 12 | fmustinput | 必录控制 | varchar | 255 |  | √ | ' ' | 必录控制 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_botp_convertpath_param |  | fid |
| 2 | idx_botp_cp_param_billnum |  | fsourcebillnumber,ftargetbillnumber |

---

## 转换路线参数-多语言表 t_botp_convertpath_param_l

- **表名称：** 转换路线参数-多语言表
- **表名：** t_botp_convertpath_param_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_botp_convertpath_param_l |  | fpkid |
| 2 | idx_botp_cp_param_l_fid |  | fid,flocaleid |
| 3 | idx_botp_cp_param_l_fname |  | fname |
