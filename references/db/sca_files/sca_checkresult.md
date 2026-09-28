# 合法性检查结果-sca_checkresult

## 单据体-多语言表 t_sca_checkresultentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_sca_checkresultentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparam | 进入页面详细参数 | text | 0 |  |  | null | 进入页面详细参数 |
| 2 | fresultdesc | 结果描述 | varchar | 255 |  | √ | ' ' | 结果描述 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fcheckdesc | 检查说明 | varchar | 2000 |  | √ | ' ' | 检查说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkresultentry_l_pkey |  | fpkid |
| 2 | idx_sca_checkresultentry_l |  | flocaleid,fentryid |

---

## 生产组织-多选基础资料表 t_sca_checkrtmorg

- **表名称：** 生产组织-多选基础资料表
- **表名：** t_sca_checkrtmorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_checkrtmorg |  | fpkid |
| 2 | idx_sca_checkrtmorg |  | fid,fbasedataid |

---

## 成本中心-多选基础资料表 t_sca_checkresultcenter

- **表名称：** 成本中心-多选基础资料表
- **表名：** t_sca_checkresultcenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkresultcenter_pkey |  | fpkid |
| 2 | idx_sca_checkresultcenter |  | fid,fbasedataid |

---

## 单据体-子表 t_sca_checkresultentry

- **表名称：** 单据体-子表
- **表名：** t_sca_checkresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitem | 检查项 | varchar | 255 |  | √ | ' ' | 检查项 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fresult | 检查结果 | varchar | 30 |  | √ | ' ' | 检查结果,枚举: 1 :通过 2 :不通过 3 :提醒 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fitemid | fitemid | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkresultentry_pkey |  | fentryid |
| 2 | idx_sca_checkresultentry |  | fid,fitemid |

---

## 合法性检查结果-主表 t_sca_checkresult

- **表名称：** 合法性检查结果-主表
- **表名：** t_sca_checkresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 5 | fcheckdate | 检查日期 | timestamp | 0 |  |  | null | 检查日期 |
| 6 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 7 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_checkresult |  | forgid,fcostaccountid,fperiodid |
| 2 | t_sca_checkresult_pkey |  | fid |
