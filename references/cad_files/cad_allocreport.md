# 分配报告-cad_allocreport

## 分配报告-主表 t_cad_allocreport

- **表名称：** 分配报告-主表
- **表名：** t_cad_allocreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrcbill | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 5 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 6 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :成功 2 :部分成功 3 :失败 4 :执行中 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 11 | freporttype | 报告类型 | varchar | 50 |  | √ | ' ' | 报告类型 |
| 12 | fusetime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 13 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 14 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 16 | fpageparam | 分配详情参数 | varchar | 255 |  | √ | ' ' | 分配详情参数 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | ftaskname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称,枚举: 1 :非生产分配 2 :辅助生产分配 3 :基本生产分配 4 :成本中心内分配 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fstarttime | 分配日期 | timestamp | 0 |  |  | null | 分配日期 |
| 24 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_allocreport |  | fid |
| 2 | idx_t_cad_allocreport |  | forgid,fmanuorgid,fcostcenterid,fcostaccountid |

---

## 结果详情-子表 t_cad_allocreportentry

- **表名称：** 结果详情-子表
- **表名：** t_cad_allocreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckdetail | 检查说明 | varchar | 1000 |  | √ | ' ' | 检查说明 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcheckitem | 检查项 | varchar | 500 |  | √ | ' ' | 检查项 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fallocresult | 分配结果 | varchar | 500 |  | √ | ' ' | 分配结果,枚举: 1 :通过 2 :不通过 3 :部分通过 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_allocreportentry |  | fentryid |
| 2 | idx_t_cad_allocreportentry |  | fid |
