# 疑似重复单据-fcs_suspectbill

## 疑似重复单据-主表 t_fcs_suspectbill

- **表名称：** 疑似重复单据-主表
- **表名：** t_fcs_suspectbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsuspectsetid | 疑似防重配置 | int8 | 64 |  | √ | 0 | 疑似防重配置 fcs_suspectset |
| 6 | fuprecordconfirm | 是否上游链路确认 | bpchar | 1 |  | √ | '0' | 是否上游链路确认 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fconfirm | 是否确认 | bpchar | 1 |  | √ | '0' | 是否确认 |
| 10 | fconfirmer | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fctrltype | 疑似防重控制 | varchar | 30 |  | √ | ' ' | 疑似防重控制,枚举: warning :预警 landing :落地 control :严控 |
| 13 | fdestdescribe | 当前单据描述 | varchar | 2000 |  | √ | ' ' | 当前单据描述 |
| 14 | fbillid | 当前单id | int8 | 64 |  | √ | 0 | 当前单id |
| 15 | fbillentityid | 当前单据类型 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fconfirmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_suspectbill |  | fid |
| 2 | idx_fcs_susbectbill |  | fconfirm,fbillid |
| 3 | idx_time_fcs_susbectbill |  | fcreatetime |

---

## 疑似重复单据-多语言表 t_fcs_suspectbill_l

- **表名称：** 疑似重复单据-多语言表
- **表名：** t_fcs_suspectbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdestdescribe | 当前单据描述 | varchar | 2000 |  | √ | ' ' | 当前单据描述 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcs_suspectbill_l |  | fid |
| 2 | pk_t_fcs_suspectbill_l |  | fpkid |

---

## 疑似重复单据体-多语言表 t_fcs_suspectbill_s_l

- **表名称：** 疑似重复单据体-多语言表
- **表名：** t_fcs_suspectbill_s_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsuspectdescribe | 疑似重复描述 | varchar | 2000 |  | √ | ' ' | 疑似重复描述 |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_suspectbill_s_l |  | fpkid |
| 2 | idx_fcs_suspectbill_s_l |  | fentryid |

---

## 疑似重复单据体-子表 t_fcs_suspectbill_s

- **表名称：** 疑似重复单据体-子表
- **表名：** t_fcs_suspectbill_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuspectdate | 疑似业务日期 | timestamp | 0 |  |  | null | 疑似业务日期 |
| 3 | fsuspectbillentityid | 疑似重复单据类型 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 4 | fsuspectbillid | 疑似重复单据id | int8 | 64 |  | √ | 0 | 疑似重复单据id |
| 5 | fsuspectdescribe | 疑似重复描述 | varchar | 2000 |  | √ | ' ' | 疑似重复描述 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsuspectbillno | 疑似重复单据编号 | varchar | 50 |  | √ | ' ' | 疑似重复单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_suspectbill_s |  | fentryid |
| 2 | idx_fcs_suspectbill_s |  | fid |
