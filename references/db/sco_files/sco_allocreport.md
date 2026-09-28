# 分配报告-sco_allocreport

## 分配报告-主表 t_sco_allocreport

- **表名称：** 分配报告-主表
- **表名：** t_sco_allocreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 5 | fsrcbill | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 6 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 7 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :成功 2 :部分成功 3 :失败 4 :执行中 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | freporttype | 报告类型 | varchar | 30 |  | √ | ' ' | 报告类型 |
| 13 | fusetime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 14 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 15 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 17 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 18 | fpageparam | 分配详情参数 | varchar | 255 |  | √ | ' ' | 分配详情参数 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | ftaskname | 任务名称 | varchar | 255 |  | √ | ' ' | 任务名称,枚举: 1 :非生产分配 2 :辅助生产分配 3 :基本生产分配 4 :成本中心内分配 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fstarttime | 分配日期 | timestamp | 0 |  |  | null | 分配日期 |
| 26 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_allocreport |  | fid |
| 2 | idx_sco_allocreport |  | forgid,fmanuorgid,fcostcenterid,fcostaccountid |

---

## 结果详情-子表 t_sco_allocreportentry

- **表名称：** 结果详情-子表
- **表名：** t_sco_allocreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckdetail | 检查说明 | varchar | 1000 |  | √ | ' ' | 检查说明 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcheckitem | 检查项 | varchar | 30 |  | √ | ' ' | 检查项 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fallocresult | 分配结果 | varchar | 30 |  | √ | ' ' | 分配结果,枚举: 1 :通过 2 :不通过 3 :部分通过 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_allocreportentry |  | fid |
| 2 | pk_sco_allocreportentry |  | fentryid |
