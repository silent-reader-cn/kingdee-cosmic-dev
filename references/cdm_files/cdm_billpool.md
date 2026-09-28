# 票据池维护-cdm_billpool

## 票据池维护-主表 t_cdm_billpool

- **表名称：** 票据池维护-主表
- **表名：** t_cdm_billpool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 4 | fname | 票据池名称 | varchar | 255 |  | √ | ' ' | 票据池名称 |
| 5 | fdispatchrule | 票据调度规则 | varchar | 30 |  | √ | ' ' | 票据调度规则,枚举: direct :直接调度 indirect :间接调度 |
| 6 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fcontacts | 银行联系人 | varchar | 255 |  | √ | ' ' | 银行联系人 |
| 9 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 10 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | varchar | 80 |  | √ | ' ' | 主数据内码 |
| 16 | ftype | 票据池类型 | varchar | 30 |  | √ | ' ' | 票据池类型,枚举: inner :内部票据池 bank :银行票据池 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fnumber | 票据池编码 | varchar | 80 |  | √ | ' ' | 票据池编码 |
| 20 | fcdate | 建立日期 | timestamp | 0 |  |  | null | 建立日期 |
| 21 | fbankid | 合作银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 22 | fcount | 成员数量 | int8 | 64 |  | √ | 0 | 成员数量 |
| 23 | fisdefault | 默认票据池 | bpchar | 1 |  | √ | '0' | 默认票据池 |
| 24 | fcompanyid | 建池收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_billpool |  | fnumber |
| 2 | pk_t_cdm_billpool |  | fid |

---

## 单据体-子表 t_cdm_billpool_entry

- **表名称：** 单据体-子表
- **表名：** t_cdm_billpool_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fcompanyid | 收付组织名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cdm_billpool_entry |  | fentryid |
| 2 | idx_cdm_billpool_entry |  | fid |

---

## 票据池维护-多语言表 t_cdm_billpool_l

- **表名称：** 票据池维护-多语言表
- **表名：** t_cdm_billpool_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 票据池名称 | varchar | 255 |  | √ | ' ' | 票据池名称 |
| 3 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_billpool_l |  | fid |
| 2 | pk_cdm_billpool_l |  | fpkid |
