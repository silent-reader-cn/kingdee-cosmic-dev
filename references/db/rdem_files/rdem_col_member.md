# 列维成员管理-rdem_col_member

## 列维成员管理-主表 t_rdem_col_member

- **表名称：** 列维成员管理-主表
- **表名：** t_rdem_col_member

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodel | 体系 | int8 | 64 |  | √ | 0 | [体系管理 rdem_model](../rdem_files/rdem_model.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 7 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [列维成员管理 rdem_col_member](../rdem_files/rdem_col_member.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fformat | 格式化 | varchar | 50 |  | √ | ' ' | 格式化,枚举: #0.00 :精确2位 #0.0000 :精确4位 #0.00000 :精确5位 #0.000000 :精确6位 #0.00000000 :精确8位 #0.0000000000 :精确10位 yyyy-MM :yyyy-MM yyyy-MM-dd :yyyy-MM-dd yyyy-MM-dd HH:mm:ss :yyyy-MM-dd HH:mm:ss yyyy :yyyy % :百分数 |
| 10 | flongnumber | 长编码 | varchar | 127 |  | √ | ' ' | 长编码 |
| 11 | fminlength | 最小长度 | int8 | 64 |  | √ | 0 | 最小长度 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmaxlength | 最大长度 | int8 | 64 |  | √ | 0 | 最大长度 |
| 18 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 19 | fdefaultvalue | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 22 | fdimension | 维度 | int8 | 64 |  | √ | 0 | 维度管理 tpo_dimension |
| 23 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: integer :整数 decimal :小数 string :字符串 date :日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_col_member_m0 |  | fmasterid |
| 2 | pk_rdem_col_member |  | fid |

---

## 列维成员管理-多语言表 t_rdem_col_member_l

- **表名称：** 列维成员管理-多语言表
- **表名：** t_rdem_col_member_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | ffullname | 长名称 | varchar | 399 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_col_member_l |  | fpkid |
| 2 | idx_rdem_col_member_l_0 |  | fid,flocaleid |

---

## 单据体-子表 t_rdem_col_member_entry

- **表名称：** 单据体-子表
- **表名：** t_rdem_col_member_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 3 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 4 | fentryformat | 格式化 | varchar | 50 |  | √ | ' ' | 格式化,枚举: #0.00 :精确2位 #0.0000 :精确4位 #0.00000 :精确5位 #0.000000 :精确6位 #0.00000000 :精确8位 #0.0000000000 :精确10位 yyyy-MM :yyyy-MM yyyy-MM-dd :yyyy-MM-dd yyyy-MM-dd HH:mm:ss :yyyy-MM-dd HH:mm:ss yyyy :yyyy % :百分数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentrymaxlength | 最大长度 | int8 | 64 |  | √ | 0 | 最大长度 |
| 7 | fentryminlength | 最小长度 | int8 | 64 |  | √ | 0 | 最小长度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_col_member_entry |  | fentryid |
| 2 | idx_rdem_col_member_entry_fk |  | fid |
