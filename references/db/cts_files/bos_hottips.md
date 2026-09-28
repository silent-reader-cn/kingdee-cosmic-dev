# 帮助文本热更新-bos_hottips

## 帮助文本热更新-主表 t_bas_hottips

- **表名称：** 帮助文本热更新-主表
- **表名：** t_bas_hottips

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsynctime | 同步时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 同步时间 |
| 3 | fkey | 控件标识 | varchar | 50 |  | √ | ' ' | 控件标识 |
| 4 | fbizcloudid | 所属云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 5 | fformtype | 表单类型 | bpchar | 1 |  | √ | '1' | 表单类型,枚举: 1 :表单 2 :列表 3 :移动表单 4 :移动列表 |
| 6 | fdata | tips内容 | text | 0 |  |  | null | tips内容 |
| 7 | faudittime | tips范围开始时间 | timestamp | 0 |  |  | null | tips范围开始时间 |
| 8 | fformid | 表单 | varchar | 36 |  | √ | ' ' | 表单 |
| 9 | fversion | 适用版本 | varchar | 30 |  | √ | ' ' | 适用版本 |
| 10 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_hottips |  | fid |
| 2 | idx_bas_hottips_formid |  | fformid,fkey,fformtype |
