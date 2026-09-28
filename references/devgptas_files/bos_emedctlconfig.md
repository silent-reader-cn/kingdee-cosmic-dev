# 嵌入式控件技能组配置-bos_emedctlconfig

## 嵌入式控件技能组配置-主表 t_gptas_emedctlonfig

- **表名称：** 嵌入式控件技能组配置-主表
- **表名：** t_gptas_emedctlonfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 技能组Id | varchar | 50 |  | √ | ' ' | 技能组Id |
| 3 | ftype | 控件类型 | varchar | 50 |  | √ | ' ' | 控件类型,枚举: |
| 4 | fisentry | 单据体控件 | bpchar | 1 |  | √ | '0' | 单据体控件 |
| 5 | fisonly | 仅当前控件类型 | bpchar | 1 |  |  | '0' | 仅当前控件类型 |
| 6 | fgroupname | 技能组名称 | varchar | 50 |  | √ | ' ' | 技能组名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gptas_emedctlonfig |  | ftype,fgroupid |
| 2 | pk_t_gptas_emedctlonfig |  | fid |
