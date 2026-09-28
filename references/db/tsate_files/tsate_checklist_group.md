# 申报检查-tsate_checklist_group

## 单据体-子表 t_tsate_checklist_body

- **表名称：** 单据体-子表
- **表名：** t_tsate_checklist_body

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjkqx | 缴款期限 | timestamp | 0 |  |  | null | 缴款期限 |
| 3 | fzsxm | 征收项目 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsbsx | 申报事项 | varchar | 200 |  | √ | ' ' | 申报事项 |
| 6 | freleasedate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 7 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 8 | fsbqx | 申报期限 | timestamp | 0 |  |  | null | 申报期限 |
| 9 | fybtse | 应补退税额 | numeric | 23 | 10 | √ | 0 | 应补退税额 |
| 10 | fskssswjgmc | 税款所属税务机关 | varchar | 80 |  | √ | ' ' | 税款所属税务机关 |
| 11 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 12 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 13 | fyjse | 应缴税额 | numeric | 23 | 10 | √ | 0 | 应缴税额 |
| 14 | fznj | 滞纳金 | numeric | 23 | 10 | √ | 0 | 滞纳金 |
| 15 | fyzpzxh | 应税凭证号 | varchar | 200 |  | √ | ' ' | 应税凭证号 |
| 16 | fyzpzzlmc | 应征凭证种类名称 | varchar | 200 |  | √ | ' ' | 应征凭证种类名称 |
| 17 | fsbjg | 云合申报清册申报状态 | varchar | 500 |  | √ | ' ' | 云合申报清册申报状态 |
| 18 | fsbrq | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 19 | fdzsph | 电子税票号 | varchar | 100 |  | √ | ' ' | 电子税票号 |
| 20 | fjkrq | 缴款日期 | timestamp | 0 |  |  | null | 缴款日期 |
| 21 | fskzt | 税款状态 | varchar | 500 |  | √ | ' ' | 税款状态 |
| 22 | fsjje | 实缴金额 | numeric | 23 | 10 | √ | 0 | 实缴金额 |
| 23 | fbodymodifierld | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 25 | fjkzt | 缴款状态 | varchar | 50 |  | √ | ' ' | 缴款状态,枚举: 2 :无需缴款 0 :未缴款 1 :已缴款 |
| 26 | fbodymodifydatefieid | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 27 | fsksx | 税款属性 | varchar | 50 |  | √ | ' ' | 税款属性 |
| 28 | fcompareresult | 状态比对结果 | varchar | 50 |  | √ | ' ' | 状态比对结果,枚举: 0 :未比对 1 :比对中 2 :无差异 3 :有差异 4 :无比对数据 5 :比对失败 |
| 29 | ftaxorgid | 主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 30 | fsbzt | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: 0 :未申报 1 :已申报 2 :申报失败 4 :无需申报 3 :申报中 5 :申报成功 6 :税局已受理 7 :已提交待清卡 8 :税局处理中 9 :待申报 16 :作废申报中 17 :作废申报已受理 18 :作废成功待申报 19 :作废申报失败 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_checklist_body_fk |  | fid |
| 2 | pk_tsate_checklist_body |  | fentryid |

---

## 申报检查-主表 t_tsate_checklist_head

- **表名称：** 申报检查-主表
- **表名：** t_tsate_checklist_head

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgxsj | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 3 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftasktype | 信息类型 | int8 | 64 |  | √ | 0 | [任务类型 tsate_tasktype](../tsate_files/tsate_tasktype.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fswjgmc | 税务机关名称（特殊） | varchar | 50 |  | √ | ' ' | 税务机关名称（特殊） |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | frqfz | 辅助日期分组字段 | timestamp | 0 |  |  | null | 辅助日期分组字段 |
| 11 | fxqzs | 税局反馈 | varchar | 50 |  | √ | ' ' | 税局反馈,枚举: 1 :详情 0 : |
| 12 | fmodifytime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 13 | fhistoryflag | 数据升级标识 | varchar | 50 |  | √ | ' ' | 数据升级标识,枚举: 1 :是 0 :否 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsjly | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :税局下载 2 :手工导入 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_checklist_head |  | fid |
| 2 | idx_tsate_checklh_org |  | forgid |
