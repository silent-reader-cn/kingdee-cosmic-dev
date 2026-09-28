# 预算使用规则-ocmem_budgetuserule

## 单据体-子表 t_ocmem_bguseruleentry

- **表名称：** 单据体-子表
- **表名：** t_ocmem_bguseruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusectrl | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: A :不控制 B :预警提示 C :强制控制 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fcontrolop | 业务操作 | varchar | 80 |  | √ | ' ' | 业务操作,枚举: |

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

---

## 预算使用规则-主表 t_ocmem_budgetuserule

- **表名称：** 预算使用规则-主表
- **表名：** t_ocmem_budgetuserule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 规则名称 | varchar | 80 |  | √ | ' ' | 规则名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fexcessvalue | 超额率/超额值 | numeric | 23 | 10 | √ | 0 | 超额率/超额值 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fdeviationtype | 偏差类型 | bpchar | 1 |  | √ | ' ' | 偏差类型,枚举: A :偏差率% B :偏差额 |
| 12 | fctrltype | 控制类型 | bpchar | 1 |  | √ | 'A' | 控制类型,枚举: A :实际数小于等于预算额 B :按偏差控制 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 15 | fbillentity | 预算适用单据 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_budgetuserule_no |  | fnumber |
| 2 | pk_ocmem_budgetuserule |  | fid |
