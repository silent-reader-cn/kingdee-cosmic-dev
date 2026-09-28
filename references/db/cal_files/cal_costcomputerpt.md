# 出库核算报告-cal_costcomputerpt

## 单据体-子表 t_cal_costrptentry

- **表名称：** 单据体-子表
- **表名：** t_cal_costrptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdividebasis | 划分依据 | varchar | 100 |  | √ | ' ' | 划分依据 |
| 3 | fcalrange | 核算范围 | varchar | 100 |  | √ | ' ' | 核算范围 |
| 4 | fpayout | 发出 | varchar | 255 |  | √ | ' ' | 发出 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fincome | 收入 | varchar | 255 |  | √ | ' ' | 收入 |
| 7 | fsettle | 结存 | varchar | 255 |  | √ | ' ' | 结存 |
| 8 | fbillnumber | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 9 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 10 | faccounttype | 计价方法 | varchar | 100 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 G :先进先出法 |
| 11 | fcaldimension | 核算维度 | varchar | 200 |  | √ | ' ' | 核算维度 |
| 12 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fwarehsid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fbilltype | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costrptentry_pkey |  | fentryid |
| 2 | idx_cal_costentry |  | fid |

---

## 出库核算报告-主表 t_cal_costrpt

- **表名称：** 出库核算报告-主表
- **表名：** t_cal_costrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 3 | fcalstatus | 结转状态 | varchar | 5 |  | √ | 'A' | 结转状态,枚举: A :结转成功 B :结转失败 C :警告 |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcalsystemid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系（已作废） bd_accountingsys](../fibd_files/bd_accountingsys.md) |
| 7 | fnextseq | 分录下个序号 | int8 | 64 |  | √ | 0 | 分录下个序号 |
| 8 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fcaltime | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |
| 10 | fisvalid | 是否有效 | bpchar | 1 |  | √ | '0' | 是否有效 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costrtp_material |  | fmaterial |
| 2 | t_cal_costrpt_pkey |  | fid |
