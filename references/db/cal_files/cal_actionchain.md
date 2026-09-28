# 核算接口功能配置-cal_actionchain

## 分录信息-子表 t_cal_actionsettingentry

- **表名称：** 分录信息-子表
- **表名：** t_cal_actionsettingentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fexeseq | 执行序号 | int8 | 64 |  | √ | 0 | 执行序号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fimplclass | 实现类 | varchar | 255 |  | √ | ' ' | 实现类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_actionst_et |  | fentryid |

---

## 核算接口功能配置-主表 t_cal_actionsetting

- **表名称：** 核算接口功能配置-主表
- **表名：** t_cal_actionsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factionname | 功能名称 | varchar | 30 |  | √ | ' ' | 功能名称,枚举: AUDIT :库存审核 UNAUDIT :库存反审核 PURWRITEOFF :采购核销 PURUNWRITEOFF :采购反核销 ADDAVERAG :实时移动成本计算 SALEWRITEOFF :销售核销 SALEUNWRITEOFF :销售反核销 SETTLEACCOUNT :存货结账 UNSETTLEACCOUNT :存货反结账 COSTADJUSTAUDIT :成本调整单审核 COSTADJUSTUNAUDIT :成本调整单反审核 COSTESTIMATECREATE :费用暂估单创建 COSTESTIMATEDELETE :费用暂估单删除 MATERIALWRITEOFF :材料核销 UNSUBMIT :撤销 RESYNC :重新同步 AUTORESYNC :自动同步 SUBMIT :提交 REESTIMATE :暂估调价 HOOKACCOUNT :钩稽入库核算 UNHOOKACCOUNT :反钩稽入库核算 APSETTLEBILLAUDIT :应付结算清单审核 FEEHOOKACCOUNT :费用分摊入库核算 FEEUNHOOKACCOUNT :费用反分摊入库核算 |
| 3 | fservicetype | 接口类型 | varchar | 30 |  | √ | ' ' | 接口类型,枚举: A :校验接口 B :业务接口 |
| 4 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 5 | fsettingnum | 配置编码 | varchar | 80 |  | √ | ' ' | 配置编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_actionst |  | fid |
