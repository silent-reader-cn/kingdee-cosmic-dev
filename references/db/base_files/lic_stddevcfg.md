# 开发服务融合版许可配置-lic_stddevcfg

## 开发服务融合版许可配置-主表 t_lic_standdevconfig

- **表名称：** 开发服务融合版许可配置-主表
- **表名：** t_lic_standdevconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitytypeid | 表单 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 3 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lic_stddevconfig_entid |  | fentitytypeid |
| 2 | idx_lic_stddevconfig_appid |  | fbizappid |
| 3 | pk_t_lic_standdevconfig |  | fid |
