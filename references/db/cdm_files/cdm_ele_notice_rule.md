# 电票签收/通知规则-cdm_ele_notice_rule

## 电票签收/通知规则-主表 t_cdm_ele_notice_rule

- **表名称：** 电票签收/通知规则-主表
- **表名：** t_cdm_ele_notice_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fenabledate | fenabledate | timestamp | 0 |  |  | null |  |
| 7 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 8 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fenablerid | fenablerid | int8 | 64 |  | √ | 0 |  |
| 15 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |
| 16 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_ele_notice_rule |  | fid |
| 2 | idx_t_cdm_ele_notice_rule |  | fnumber |

---

## 适用组织-子表 t_cdm_ele_org_entry

- **表名称：** 适用组织-子表
- **表名：** t_cdm_ele_org_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuorgid | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_ele_org_entry |  | fentryid |
| 2 | idx_t_cdm_ele_org_entry |  | fid |

---

## 规则信息-子表 t_cdm_ele_rule_entity

- **表名称：** 规则信息-子表
- **表名：** t_cdm_ele_rule_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  |  | null | 备注 |
| 3 | frefuseremark | 拒收意见 | varchar | 50 |  |  | null | 拒收意见 |
| 4 | fdatafilter | 适用条件大文本 | text | 0 |  |  | null | 适用条件大文本 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdatafilterdesc | 适用条件 | varchar | 1024 |  | √ | ' ' | 适用条件 |
| 7 | fdatafilter_tag | 适用条件大文本_详情 | text | 0 |  |  | null | 适用条件大文本_详情 |
| 8 | fsavenotifi | 通知方案大文本 | text | 0 |  |  | null | 通知方案大文本 |
| 9 | fnotifische | 通知方案 | varchar | 1024 |  | √ | ' ' | 通知方案 |
| 10 | fsavenotifi_tag | 通知方案大文本_详情 | text | 0 |  |  | null | 通知方案大文本_详情 |
| 11 | frulesname | 规则项名称 | varchar | 255 |  | √ | ' ' | 规则项名称 |
| 12 | fhandlescheme | 处理方案 | varchar | 30 |  | √ | '0' | 处理方案,枚举: noticeclaim :通知认领 notesignin :签收 notesigninreject :拒收 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_ele_rule_entity |  | fentryid |
| 2 | idx_t_cdm_ele_rule_entity |  | fid |

---

## 电票签收/通知规则-多语言表 t_cdm_ele_notice_rule_l

- **表名称：** 电票签收/通知规则-多语言表
- **表名：** t_cdm_ele_notice_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 255 |  | √ | ' ' | 规则名称 |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cdm_ele_notice_rule_l |  | fid |
| 2 | pk_t_cdm_ele_notice_rule_l |  | fpkid |
