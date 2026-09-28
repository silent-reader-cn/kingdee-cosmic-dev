# 预算使用规则-ocmem_budgetuserule

## 统一控制方式分录-子表 t_ocmem_bguseruleentry

- **表名称：** 统一控制方式分录-子表
- **表名：** t_ocmem_bguseruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusectrl | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: A :不控制 B :预警提示 C :强制控制 |
| 3 | fcontrolopname | 业务操作名称 | varchar | 255 |  | √ | ' ' | 业务操作名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcontrolop | 业务操作 | varchar | 80 |  | √ | ' ' | 业务操作,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_bguseruleentry |  | fentryid |
| 2 | idx_ocmem_bguseruleentry_id |  | fid |

---

## 预算使用规则-主表 t_ocmem_budgetuserule

- **表名称：** 预算使用规则-主表
- **表名：** t_ocmem_budgetuserule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 80 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | famountcolname | 控制数据 | varchar | 255 |  | √ | ' ' | 控制数据,枚举: |
| 5 | fexcessvalue | 超额率/超额值 | numeric | 23 | 10 | √ | 0 | 超额率/超额值 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | famountcol | 控制数据字段名称 | varchar | 50 |  | √ | ' ' | 控制数据字段名称 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdeviationtype | 偏差类型 | bpchar | 1 |  | √ | ' ' | 偏差类型,枚举: A :偏差率% B :偏差额 |
| 14 | fctrltype | 控制类型 | bpchar | 1 |  | √ | 'A' | 控制类型,枚举: A :实际数小于等于预算额 B :按偏差控制 C :承担部门+产品金额不超预算 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 17 | fbillentity | 预算适用单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_budgetuserule_no |  | fnumber |
| 2 | pk_ocmem_budgetuserule |  | fid |

---

## 按条件控制分录-子表 t_ocmem_bgcondentry

- **表名称：** 按条件控制分录-子表
- **表名：** t_ocmem_bgcondentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconexcessvalue | 超额率/超额值 | numeric | 23 | 10 | √ | 0 | 超额率/超额值 |
| 3 | fcontrolopname | 业务操作名称 | varchar | 255 |  | √ | ' ' | 业务操作名称 |
| 4 | fdatafilter | 条件 | text | 0 |  |  | null | 条件 |
| 5 | fbudgetfilter | 预算条件 | text | 0 |  |  | null | 预算条件 |
| 6 | fbudgetdatafilter | 预算条件 | text | 0 |  |  | null | 预算条件 |
| 7 | fmulcombofield | 预算控制依据 | text | 0 |  |  | null | 预算控制依据,枚举: |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fconditionusectrl | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: A :不控制 B :预警提示 C :强制控制 |
| 10 | fcontrolop | 业务操作 | varchar | 255 |  | √ | ' ' | 业务操作,枚举: |
| 11 | fbudgetfilter_tag | 预算条件_详情 | text | 0 |  |  | null | 预算条件_详情 |
| 12 | fmulcombofieldname | 预算控制依据 | varchar | 255 |  | √ | ' ' | 预算控制依据 |
| 13 | fctrltype | 控制类型 | bpchar | 1 |  | √ | ' ' | 控制类型,枚举: A :实际数小于等于预算额 B :按偏差控制 |
| 14 | fcondeviationtype | 偏差类型 | bpchar | 1 |  | √ | ' ' | 偏差类型,枚举: A :偏差率% B :偏差额 |
| 15 | fconditionfilter_tag | 条件_详情 | text | 0 |  |  | null | 条件_详情 |
| 16 | fbudgetdatafilter_tag | fbudgetdatafilter_tag | text | 0 |  |  | null |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fconditionfilter | 条件 | text | 0 |  |  | null | 条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_bgcondentry |  | fentryid |
| 2 | idx_ocmem_bgcondentry |  | fid |

---

## 预算使用规则-多语言表 t_ocmem_budgetuserule_l

- **表名称：** 预算使用规则-多语言表
- **表名：** t_ocmem_budgetuserule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 规则名称 | varchar | 80 |  | √ | ' ' | 规则名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_budgetuserule_l |  | fpkid |
| 2 | idx_ocmem_budgetuserulel_flid |  | fid,flocaleid |
