# 凭证生成报告-ai_buildreport

## 凭证生成报告-主表 t_ai_buildreport

- **表名称：** 凭证生成报告-主表
- **表名：** t_ai_buildreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransid | 事务标识 | varchar | 36 |  | √ | ' ' | 事务标识 |
| 3 | fglvoucherno | 凭证编码 | varchar | 30 |  | √ | ' ' | 凭证编码 |
| 4 | fexceptioninfo | 异常堆栈信息 | text | 0 |  |  | ' ' | 异常堆栈信息 |
| 5 | fbuildvouchertype | 凭证生成来源方式 | bpchar | 1 |  | √ | ' ' | 凭证生成来源方式,枚举: 0 :生成业务凭证和总账凭证 1 :仅生成业务凭证 2 :业务凭证生成总账凭证 |
| 6 | faimodel | AI记账模型 | int8 | 64 |  | √ | 0 | [AI记账模型 ai_accountingmodel](../ai_files/ai_accountingmodel.md) |
| 7 | failoginfo | AI生成日志 | varchar | 2000 |  | √ | ' ' | AI生成日志 |
| 8 | fbuildtype | 生成方式 | varchar | 30 |  | √ | ' ' | 生成方式,枚举: A :单据生成凭证操作 B :定时自动生成方案 C :凭证生成向导操作 D :实时自动生成方案 E :自动结账调用生成凭证 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fglvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 11 | ferrorresult | 异常信息 | varchar | 200 |  | √ | ' ' | 异常信息 |
| 12 | fsourcebillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 13 | faccountingmode | 记账模式 | bpchar | 1 |  | √ | '0' | 记账模式,枚举: 0 :模板记账 1 :AI记账 |
| 14 | fbizvoucherno | 业务凭证编码 | varchar | 80 |  | √ | ' ' | 业务凭证编码 |
| 15 | fbuildtasktag | 任务标识 | varchar | 36 |  | √ | ' ' | 任务标识 |
| 16 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 17 | ftemplateid | 凭证模板 | int8 | 64 |  | √ | 0 | [凭证模板 ai_vchtemplate](../ai_files/ai_vchtemplate.md) |
| 18 | fsourcebilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fbuildstate | 状态 | varchar | 2 |  | √ | ' ' | 状态,枚举: 0 :已生成 1 :未生成 |
| 21 | fsourcesys | 来源系统（废弃） | varchar | 36 |  | √ | ' ' | 来源系统（废弃） |
| 22 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 23 | fexceptioninfo_tag | 异常堆栈信息_详情 | text | 0 |  |  | null | 异常堆栈信息_详情 |
| 24 | fisexceptionreport | 是否异常报告 | bpchar | 1 |  | √ | '0' | 是否异常报告 |
| 25 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 26 | fstrsourcebillid | 来源单据id（字符型） | varchar | 18 |  | √ | ' ' | 来源单据id（字符型） |
| 27 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 28 | fautovoucherschema | 自动生成凭证方案 | int8 | 64 |  | √ | 0 | [自动生成凭证方案 ai_autogenschema](../ai_files/ai_autogenschema.md) |
| 29 | fbizvoucherid | 业务凭证id | int8 | 64 |  | √ | 0 | 业务凭证id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_buildreport_tag |  | fbuildtasktag |
| 2 | t_ai_buildreport_pkey |  | fid |
| 3 | idx_ai_buildreport |  | fbookid,fperiodid |
| 4 | idx_ai_buildreport_s |  | fsourcebillid,fsourcebillno |
| 5 | idx_ai_buildreport_gv |  | fglvoucherid |
| 6 | idx_ai_buildreport_ts |  | fcreatetime,fsourcebill |

---

## 报告明细-子表 t_ai_buildreportentry

- **表名称：** 报告明细-子表
- **表名：** t_ai_buildreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 提示信息 | varchar | 1000 |  |  | ' ' | 提示信息 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcheckitem | 检查项 | varchar | 5 |  | √ | ' ' | 检查项,枚举: 0 :凭证模板 1 :凭证字 2 :账簿 3 :科目 4 :核算维度 5 :影响因素 6 :金额 7 :币别 8 :汇率 9 :摘要 10 :记账日期 11 :单据 12 :科目核算币别 13 :业务凭证 14 :到期日 15 :总账凭证 16 :数量核算 17 :分录筛选条件 18 :AI记账 99 :其他 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ferrlevel | 错误级别 | varchar | 5 |  | √ | ' ' | 错误级别,枚举: 0 :警告 1 :异常 2 :错误 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_buildreportentry |  | fid,fcheckitem,ferrlevel |
| 2 | t_ai_buildreportentry_pkey |  | fentryid |
