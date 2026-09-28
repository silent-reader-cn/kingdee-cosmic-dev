# 全网库存集成配置-ococic_integrationconfig

## 全网库存集成配置-主表 t_ococic_integratconfig

- **表名称：** 全网库存集成配置-主表
- **表名：** t_ococic_integratconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvlastsynctime | 库存最后同步时间 | timestamp | 0 |  |  | null | 库存最后同步时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ococic_integratconfig |  | fid |
| 2 | idx_ococic_inteconfig_synctime |  | finvlastsynctime |
