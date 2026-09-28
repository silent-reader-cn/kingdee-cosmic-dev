# 差异分摊计算报告-sca_restore_calcreport

## 差异分摊计算报告-主表 t_sca_diffalloccountrpt

- **表名称：** 差异分摊计算报告-主表
- **表名：** t_sca_diffalloccountrpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ftaskname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 9 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 10 | fstarttime | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fnextpagepara | 页面携带参数 | varchar | 1000 |  | √ | ' ' | 页面携带参数 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | ftype | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :警告 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | freporttype | 报告类型 | varchar | 30 |  | √ | ' ' | 报告类型,枚举: 1 :在产品 2 :完工产品 |
| 17 | fnextpagepara_tag | 页面携带参数_详情 | text | 0 |  |  | null | 页面携带参数_详情 |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fusetime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: 1 :合法性检查报告 2 :差异分摊计算报告 |
| 23 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_diffalloccountrpt |  | fid |
| 2 | idx_sca_diffalloccountrpt |  | forgid,fcostaccountid |

---

## 步骤明细-子表 t_sca_alloccountrpt_step

- **表名称：** 步骤明细-子表
- **表名：** t_sca_alloccountrpt_step

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcnsmtime | 耗时（毫秒） | varchar | 60 |  | √ | ' ' | 耗时（毫秒） |
| 4 | fsubparam | 子页面参数 | varchar | 255 |  | √ | ' ' | 子页面参数 |
| 5 | fdetailconfigid | 明细配置ID | int8 | 64 |  | √ | 0 | 明细配置ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fresult | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :通过 6 :错误 7 :警告 |
| 8 | fbigtext_tag | 提示_详情 | text | 0 |  |  | null | 提示_详情 |
| 9 | fsubparam_tag | 子页面参数_详情 | text | 0 |  |  | null | 子页面参数_详情 |
| 10 | fbigtext | 提示 | varchar | 255 |  | √ | ' ' | 提示 |
| 11 | fdetail | 执行详情 | varchar | 255 |  | √ | ' ' | 执行详情 |
| 12 | fsubnextentity | 子页面 | varchar | 60 |  | √ | ' ' | 子页面 |
| 13 | fitem | 详细步骤 | varchar | 60 |  | √ | ' ' | 详细步骤 |
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
| 1 | idx_sca_alloccountrpt_step |  | fid |
| 2 | pk_t_sca_alloccountrpt_step |  | fentryid |
