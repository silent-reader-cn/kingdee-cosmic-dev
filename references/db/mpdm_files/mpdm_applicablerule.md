# 适用规则-mpdm_applicablerule

## 适用规则-多语言表 t_mpdm_applicablerule_l

- **表名称：** 适用规则-多语言表
- **表名：** t_mpdm_applicablerule_l

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
| 1 | pk_mpdm_applicablerule_l |  | fpkid |
| 2 | idx_mpdm_applicablerule_l |  | fid,flocaleid |

---

## 适用规则-主表 t_mpdm_applicablerule

- **表名称：** 适用规则-主表
- **表名：** t_mpdm_applicablerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | frulecondition | 适用条件 | varchar | 50 |  | √ | ' ' | 适用条件,枚举: A :必选 B :按需确认 C :实体对象 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_applicablerule |  | fid |
| 2 | idx_applicablerule_number |  | fnumber |

---

## 适用规则-子表 t_mpdm_appruleentry

- **表名称：** 适用规则-子表
- **表名：** t_mpdm_appruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterrule | 取数条件 | varchar | 2000 |  | √ | ' ' | 取数条件 |
| 3 | ffilterrulevalue | 取数条件值 | varchar | 255 |  | √ | ' ' | 取数条件值 |
| 4 | ffilterrulevalue_tag | 取数条件值_详情 | text | 0 |  |  | null | 取数条件值_详情 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fobjectentity | 实体名称 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_appruleentry |  | fentryid |
| 2 | idx_mpdm_appruleentry_fk |  | fid |
