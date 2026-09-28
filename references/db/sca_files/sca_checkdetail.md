# 标准成本核算合法性检查结果明细-sca_checkdetail

## 单据体-子表 t_sca_checkdetailentry

- **表名称：** 单据体-子表
- **表名：** t_sca_checkdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrycostcenterid | 成本中心编码 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | fcheckdetail | 检查明细 | varchar | 1000 |  | √ | ' ' | 检查明细 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkdetailentry_pkey |  | fentryid |
| 2 | idx_sca_checkdetailentry |  | fentrycostcenterid,fid |

---

## 标准成本核算合法性检查结果明细-主表 t_sca_checkdetail

- **表名称：** 标准成本核算合法性检查结果明细-主表
- **表名：** t_sca_checkdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckitemdesc | 检查项 | varchar | 255 |  | √ | ' ' | 检查项 |
| 3 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 6 | fcalcdate | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 7 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | 任务 |
| 8 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fitemid | 检查项 | int8 | 64 |  | √ | 0 | 检查项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkdetail_pkey |  | fid |
| 2 | idx_sca_checkdetail |  | forgid,fcostaccountid,fperiodid |

---

## 成本中心-多选基础资料表 t_sca_checkdetailcenter

- **表名称：** 成本中心-多选基础资料表
- **表名：** t_sca_checkdetailcenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_checkdetailcenter_pkey |  | fpkid |
| 2 | idx_sca_checkdetailcenter |  | fid,fbasedataid |
