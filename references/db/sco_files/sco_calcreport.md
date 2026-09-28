# 计算报告-sco_calcreport

## 异常差异数据-子表 t_sco_calcrptexpentry

- **表名称：** 异常差异数据-子表
- **表名：** t_sco_calcrptexpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 3 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdifferentratio | 差异率（%） | numeric | 23 | 10 | √ | 0 | 差异率（%） |
| 6 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 7 | fdifferentmoney | 差异金额 | numeric | 23 | 10 | √ | 0 | 差异金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_calcrptexpentry |  | fentryid |
| 2 | idx_sco_calcrptexpentry |  | fid,fcostobjectid |

---

## 计算报告-主表 t_sco_calcrpt

- **表名称：** 计算报告-主表
- **表名：** t_sco_calcrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmanuorgid | fmanuorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | ftaskname | 任务名称 | varchar | 255 |  | √ | ' ' | 任务名称 |
| 10 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 11 | fstarttime | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fnextpagepara | 页面携带参数 | varchar | 2000 |  | √ | ' ' | 页面携带参数 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ftype | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :警告 |
| 16 | fexecutor | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 18 | freporttype | 报告类型 | varchar | 30 |  | √ | ' ' | 报告类型,枚举: 1 :期末成本计算 2 :完工产品结算 3 :完工产品结算（工单关闭，自动执行） |
| 19 | fnextpagepara_tag | 页面携带参数_详情 | text | 0 |  |  | null | 页面携带参数_详情 |
| 20 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fusetime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 22 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_calcrpt |  | faccountorg,fcostaccountid,fperiodid,fstarttime |
| 2 | pk_sco_calcrpt |  | fid |

---

## 步骤明细-子表 t_sco_calcrptdtentry

- **表名称：** 步骤明细-子表
- **表名：** t_sco_calcrptdtentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcnsmtime | 耗时（毫秒） | int8 | 64 |  | √ | 0 | 耗时（毫秒） |
| 4 | fsubparam | 子页面参数 | varchar | 1000 |  | √ | ' ' | 子页面参数 |
| 5 | fdetailconfigid | 明细配置ID | int8 | 64 |  | √ | 0 | 明细配置ID |
| 6 | ftip | 提示 | varchar | 512 |  | √ | ' ' | 提示 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdetailstep | 详细步骤 | varchar | 255 |  | √ | ' ' | 详细步骤 |
| 9 | fsubparam_tag | 子页面参数_详情 | text | 0 |  |  | null | 子页面参数_详情 |
| 10 | fdtstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :通过 6 :错误 7 :警告 |
| 11 | fdetail | 执行详情 | varchar | 512 |  | √ | ' ' | 执行详情 |
| 12 | fsubnextentity | 子页面 | varchar | 50 |  | √ | ' ' | 子页面 |
| 13 | ferrlog | 错误日志 | varchar | 512 |  | √ | ' ' | 错误日志 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fsubstarttime | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_calcrptdtentry |  | fentryid |
| 2 | idx_sco_calcrptdtentry |  | fid,fdetailconfigid |

---

## 成本中心-多选基础资料表 t_sco_calcrptcenter

- **表名称：** 成本中心-多选基础资料表
- **表名：** t_sco_calcrptcenter

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
| 1 | idx_sco_calcrptcenter |  | fid,fbasedataid |
| 2 | pk_sco_calcrptcenter |  | fpkid |

---

## 生产组织-多选基础资料表 t_sco_calcrptmorg

- **表名称：** 生产组织-多选基础资料表
- **表名：** t_sco_calcrptmorg

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
| 1 | idx_sco_calcrptmorg |  | fid,fbasedataid |
| 2 | pk_sco_calcrptmorg |  | fpkid |
