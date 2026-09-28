# 票据锁规则-cdm_lockrule

## 票据锁规则-主表 t_cdm_lockrule

- **表名称：** 票据锁规则-主表
- **表名：** t_cdm_lockrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fworkdaynumber | 工作日天数 | int8 | 64 |  | √ | 0 | 工作日天数 |
| 4 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 5 | flocktimeslimit | 票据锁定次数限制 | bpchar | 1 |  | √ | '0' | 票据锁定次数限制 |
| 6 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 9 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | varchar | 80 |  | √ | ' ' | 主数据内码 |
| 15 | fovertimeunlock | 超时自动解锁 | bpchar | 1 |  | √ | '0' | 超时自动解锁 |
| 16 | flockamountlimit | 票据锁定张数限制 | bpchar | 1 |  | √ | '0' | 票据锁定张数限制 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fmaxlocktimes | 最大锁定次数 | int8 | 64 |  | √ | 0 | 最大锁定次数 |
| 21 | fmaxlockamount | 最大锁定张数 | int8 | 64 |  | √ | 0 | 最大锁定张数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_lockrule |  | fnumber |
| 2 | pk_cdm_lockrule |  | fid |

---

## 票据锁规则-多语言表 t_cdm_lockrule_l

- **表名称：** 票据锁规则-多语言表
- **表名：** t_cdm_lockrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_lockrule_l |  | fid |
| 2 | pk_cdm_lockrule_l |  | fpkid |
