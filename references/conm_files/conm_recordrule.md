# 履行登记规则-conm_recordrule

## 履行登记规则-主表 t_conm_recordrule

- **表名称：** 履行登记规则-主表
- **表名：** t_conm_recordrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fperformbill | 履行单据 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | frecordbill | 登记单据 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fissys | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 14 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 15 | fnumber | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_conm_recordrule |  | fid |
| 2 | idx_conm_recordrule_num |  | fnumber |

---

## 操作控制-子表 t_conm_recordrule_oe

- **表名称：** 操作控制-子表
- **表名：** t_conm_recordrule_oe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecmode | 登记方式 | varchar | 5 |  | √ | ' ' | 登记方式,枚举: A :正向 B :反向 C :差额 D :正向&反向 |
| 3 | frectype | 登记类型 | varchar | 5 |  | √ | ' ' | 登记类型,枚举: A :登记 B :删除 |
| 4 | foptionkey | 操作标识 | varchar | 80 |  | √ | ' ' | 操作标识 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | foptionname | 操作名称 | varchar | 80 |  | √ | ' ' | 操作名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_conm_recordrule_oe |  | fentryid |
| 2 | idx_conm_recordrule_oe_fid |  | fid |

---

## 履行登记规则-多语言表 t_conm_recordrule_l

- **表名称：** 履行登记规则-多语言表
- **表名：** t_conm_recordrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_conm_recordrule_l |  | fpkid |
| 2 | idx_conm_recordrule_l_fid |  | fid,flocaleid |

---

## 字段映射-子表 t_conm_recordrule_fe

- **表名称：** 字段映射-子表
- **表名：** t_conm_recordrule_fe

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fperformfield | 履行单据字段 | varchar | 255 |  | √ | ' ' | 履行单据字段 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fperformfieldname | 履行单据字段名称 | varchar | 255 |  | √ | ' ' | 履行单据字段名称 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frecordfieldname | 登记单据字段名称 | varchar | 255 |  | √ | ' ' | 登记单据字段名称 |
| 7 | frecordfield | 登记单据字段 | varchar | 255 |  | √ | ' ' | 登记单据字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conm_recordrule_fe_fid |  | fid |
| 2 | pk_t_conm_recordrule_fe |  | fentryid |
