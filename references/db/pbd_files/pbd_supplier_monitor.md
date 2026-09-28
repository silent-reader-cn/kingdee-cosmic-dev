# 供应商监控池-pbd_supplier_monitor

## 供应商清单-子表 t_pbd_monitor_entryentity

- **表名称：** 供应商清单-子表
- **表名：** t_pbd_monitor_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 监控备注 | varchar | 255 |  | √ | ' ' | 监控备注 |
| 3 | fmonitorbeforetime | 监控开始时间 | timestamp | 0 |  |  | null | 监控开始时间 |
| 4 | fmonitoraftertime | 监控结束时间 | timestamp | 0 |  |  | null | 监控结束时间 |
| 5 | fsuppliername | 供应商名称 | varchar | 200 |  | √ | ' ' | 供应商名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmonitorstatus | 监控状态 | bpchar | 1 |  | √ | ' ' | 监控状态,枚举: A :未监控 B :监控中 C :停止监控 |
| 9 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_monitor_entryentity |  | fentryid |
| 2 | idx_pbd_monitor_entry_fid_fseq |  | fid,fseq |

---

## 供应商监控池-主表 t_pbd_monitor

- **表名称：** 供应商监控池-主表
- **表名：** t_pbd_monitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 监控维度分组 | int8 | 64 |  | √ | 0 | [监控维度分组 pbd_monitor_group](../pbd_files/pbd_monitor_group.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fopttype | 操作类型 | bpchar | 1 |  | √ | '1' | 操作类型,枚举: 0 :暂停监控 1 :新增企业 2 :修改分组 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fjobid | jobid | varchar | 100 |  | √ | ' ' | jobid |
| 9 | forgid | 审批组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fisbindurl | 是否已绑定回调 | bpchar | 1 |  | √ | '0' | 是否已绑定回调 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fgroupidstr | 第三方分组id | varchar | 50 |  | √ | ' ' | 第三方分组id |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmonitortype | 监控类型 | bpchar | 1 |  | √ | '0' | 监控类型,枚举: 0 :企业监控 1 :企业监控 L2 2 :企业监控 L3 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 审批单编号 | varchar | 80 |  | √ | ' ' | 审批单编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_monitor_fbillno |  | fbillno |
| 2 | pk_pbd_monitor |  | fid |
