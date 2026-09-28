# 指标引用关系（规则引擎）-plm_rengine_targetref

## 指标引用关系（规则引擎）-主表 t_plm_egn_targetref

- **表名称：** 指标引用关系（规则引擎）-主表
- **表名：** t_plm_egn_targetref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetid | 指标 | int8 | 64 |  | √ | 0 | [指标管理 plm_rengine_target](../plmsm_files/plm_rengine_target.md) |
| 3 | fdesignruleid | 设计时规则 | int8 | 64 |  | √ | 0 | [规则设计（规则引擎） plm_rengine_ruledesign](../plmsm_files/plm_rengine_ruledesign.md) |
| 4 | fpolicyid | 策略 | int8 | 64 |  | √ | 0 | [规则设计（规则引擎） plm_rengine_ruledesign](../plmsm_files/plm_rengine_ruledesign.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_targetref_prt |  | fpolicyid,fdesignruleid,ftargetid |
| 2 | pk_plm_egn_targetref |  | fid |
