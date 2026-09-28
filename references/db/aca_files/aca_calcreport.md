# 成本计算合法性检查报告-aca_calcreport

## 步骤明细-多语言表 t_aca_calcreportentry_l

- **表名称：** 步骤明细-多语言表
- **表名：** t_aca_calcreportentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparam | 进入页面详细参数 | varchar | 255 |  | √ | ' ' | 进入页面详细参数 |
| 2 | fresultdesc | 结果描述 | varchar | 255 |  | √ | ' ' | 结果描述 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_calcreportentry_l |  | fentryid,flocaleid,fparam |
| 2 | pk_t_aca_calcreportentry_l |  | fpkid |

---

## 步骤明细-子表 t_aca_calcreportentry

- **表名称：** 步骤明细-子表
- **表名：** t_aca_calcreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcnsmtime | 耗时（毫秒） | varchar | 255 |  |  | '0' | 耗时（毫秒） |
| 3 | fsubparam | 子页面参数 | varchar | 4000 |  | √ | ' ' | 子页面参数 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fresult | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :通过 6 :错误 7 :警告 |
| 6 | fbigtext_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 7 | fbigtext | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fitemtype | 检查项类型 | bpchar | 1 |  | √ | ' ' | 检查项类型,枚举: 1 :成本计算前 2 :出库核算前 3 :成本计算后 |
| 9 | fsubnextentity | 子页面 | varchar | 255 |  | √ | ' ' | 子页面 |
| 10 | fitemnumber | 检查项编码 | varchar | 50 |  | √ | ' ' | 检查项编码 |
| 11 | fitem | 详细步骤 | varchar | 255 |  | √ | ' ' | 详细步骤 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcheckdesc | 错误日志 | varchar | 255 |  | √ | ' ' | 错误日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_calcreportentry |  | fid,fseq,fcheckdesc |
| 2 | pk_t_aca_calcreportentry |  | fentryid |

---

## 成本计算合法性检查报告-主表 t_aca_calcreport

- **表名称：** 成本计算合法性检查报告-主表
- **表名：** t_aca_calcreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fcalcdate | 计算日期 | timestamp | 0 |  |  | null | 计算日期 |
| 9 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fexecutor | fexecutor | int8 | 64 |  | √ | 0 |  |
| 13 | ftype | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :警告 |
| 14 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 15 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 16 | fusetime | 耗时（秒） | int8 | 64 |  | √ | 0 | 耗时（秒） |
| 17 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbilltype | 任务名称 | varchar | 30 |  | √ | ' ' | 任务名称,枚举: 1 :成本计算合法性检查 2 :成本计算 |
| 20 | fexecutorid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_calcreport |  | forgid,fcostaccountid |
| 2 | pk_t_aca_calcreport |  | fid |

---

## 子单据体-子表 t_aca_calcreportsubentry

- **表名称：** 子单据体-子表
- **表名：** t_aca_calcreportsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fobjtypeid | 对象类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 2 | fdetailinfo | 详情 | varchar | 500 |  | √ | ' ' | 详情 |
| 3 | fisrepaired | 是否已修复 | bpchar | 1 |  | √ | ' ' | 是否已修复 |
| 4 | fobjid | 异常对象id | int8 | 64 |  | √ | 0 | 异常对象id |
| 5 | fextralinfo | 其他信息 | varchar | 500 |  | √ | ' ' | 其他信息 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fobjdes | 对象描述 | varchar | 500 |  | √ | ' ' | 对象描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aca_calcreportsubentry |  | fdetailid |
| 2 | idx_aca_calcreportsubentry |  | fentryid |
