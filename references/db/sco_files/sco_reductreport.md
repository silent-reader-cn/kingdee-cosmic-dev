# 还原计算报告-sco_reductreport

## 还原计算报告-主表 t_sco_reductrpt

- **表名称：** 还原计算报告-主表
- **表名：** t_sco_reductrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fprdorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ftaskname | 任务名称 | varchar | 255 |  | √ | ' ' | 任务名称 |
| 9 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fstarttime | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fnextpagepara | 页面携带参数 | varchar | 2000 |  | √ | ' ' | 页面携带参数 |
| 14 | ftype | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 7 :警告 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 17 | freporttype | 报告类型 | varchar | 30 |  | √ | ' ' | 报告类型,枚举: 1 :在产品 2 :完工产品 |
| 18 | fnextpagepara_tag | 页面携带参数_详情 | text | 0 |  |  | null | 页面携带参数_详情 |
| 19 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fusetime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 21 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: 1 :合法性检查报告 2 :差异分摊计算报告 |
| 22 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_reductrpt |  | forgid,fcostaccountid,fperiodid |
| 2 | pk_sco_reductrpt |  | fid |

---

## 关联账簿-多选基础资料表 t_sco_reductrptacsub

- **表名称：** 关联账簿-多选基础资料表
- **表名：** t_sco_reductrptacsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_reductrptacsub |  | fid,fbasedataid |
| 2 | pk_sco_reductrptacsub |  | fpkid |

---

## 步骤明细-子表 t_sco_reductrptentry

- **表名称：** 步骤明细-子表
- **表名：** t_sco_reductrptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcnsmtime | 耗时（毫秒） | varchar | 80 |  | √ | ' ' | 耗时（毫秒） |
| 4 | fsubparam | 子页面参数 | varchar | 255 |  | √ | ' ' | 子页面参数 |
| 5 | fdetailconfigid | 明细配置ID | int8 | 64 |  | √ | 0 | 明细配置ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fresult | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :通过 6 :错误 7 :警告 |
| 8 | fbigtext_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 9 | fsubparam_tag | 子页面参数_详情 | text | 0 |  |  | null | 子页面参数_详情 |
| 10 | fbigtext | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fdetail | 执行详情 | varchar | 255 |  | √ | ' ' | 执行详情 |
| 12 | fsubnextentity | 子页面 | varchar | 80 |  | √ | ' ' | 子页面 |
| 13 | fitem | 详细步骤 | varchar | 80 |  | √ | ' ' | 详细步骤 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fsubstarttime | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 16 | fcheckdesc | 错误日志 | varchar | 255 |  | √ | ' ' | 错误日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_reductrptentry |  | fentryid |
| 2 | idx_sco_reductrptentry |  | fid,fentryid |
