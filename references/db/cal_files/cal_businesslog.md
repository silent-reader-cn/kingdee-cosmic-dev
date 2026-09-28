# 核算业务处理日志-cal_businesslog

## 核算业务处理日志-主表 t_cal_businesslog

- **表名称：** 核算业务处理日志-主表
- **表名：** t_cal_businesslog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalstatus | 核算处理状态 | bpchar | 1 |  | √ | 'A' | 核算处理状态,枚举: A :成功 B :失败 C :处理中 |
| 3 | fexetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 4 | fisclose | 是否关闭 | bpchar | 1 |  | √ | ' ' | 是否关闭 |
| 5 | flog_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 6 | ftimes | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 7 | fbizentityobjectid | 业务对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fparammap | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fentrykey | fentrykey | varchar | 80 |  | √ | ' ' |  |
| 11 | factionname | 功能名称 | varchar | 80 |  | √ | ' ' | 功能名称,枚举: AUDIT :库存审核 UNAUDIT :库存反审核 SETTLEACCOUNT :存货结账 UNSETTLEACCOUNT :存货反结账 COSTESTIMATECREATE :费用暂估单创建 COSTESTIMATEDELETE :费用暂估单删除 MATERIALWRITEOFF :材料核销 RESYNC :重新同步 REESTIMATE :暂估调价 HOOKACCOUNT :勾稽入库核算 UNHOOKACCOUNT :反勾稽入库核算 APSETTLEBILLAUDIT :应付结算清单审核 FEEHOOKACCOUNT :费用分摊入库核算 FEEUNHOOKACCOUNT :费用反分摊入库核算 |
| 12 | fparammap_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |
| 13 | fservicetype | 接口类型 | varchar | 5 |  | √ | ' ' | 接口类型,枚举: A :校验接口 B :业务接口 |
| 14 | flog | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 15 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 16 | fsuccess | 业务处理状态 | bpchar | 1 |  | √ | '0' | 业务处理状态,枚举: 0 :失败 1 :成功 2 :运行中 3 :业务失败 4 :系统失败 5 :警告 |
| 17 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 18 | fclosereason | 关闭原因 | varchar | 1024 |  | √ | ' ' | 关闭原因 |
| 19 | fbizbillnumber | 业务单据编码 | varchar | 80 |  | √ | ' ' | 业务单据编码 |
| 20 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 21 | fbizbillentryid | fbizbillentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_businesslog_ebo |  | fexetime,fbookdate,forgid |
| 2 | pk_cal_businesslog |  | fid |
| 3 | idx_cal_businesslog_fparam |  | fparammap |
| 4 | idx_cal_businesslog_bizbillid |  | fbizbillid |

---

## 单据体-子表 t_cal_businesslogentry

- **表名称：** 单据体-子表
- **表名：** t_cal_businesslogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostrecordeid | 核算成本记录分录id | int8 | 64 |  | √ | 0 | 核算成本记录分录id |
| 3 | ferrorinfo | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ferrorinfo_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_businesslogentry_fid |  | fid |
| 2 | idx_cal_businesslogentry_frceid |  | fcostrecordeid |
| 3 | pk_cal_businesslogentry |  | fentryid |

---

## 核算业务处理日志-多语言表 t_cal_businesslog_l

- **表名称：** 核算业务处理日志-多语言表
- **表名：** t_cal_businesslog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclosereason | 关闭原因 | varchar | 1024 |  | √ | ' ' | 关闭原因 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_businesslog_l |  | fpkid |
| 2 | idx_cal_businesslog_l_id |  | fid,flocaleid |
