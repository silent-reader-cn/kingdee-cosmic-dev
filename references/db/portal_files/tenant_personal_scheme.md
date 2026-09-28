# 个性化方案实体-tenant_personal_scheme

## 个性化方案实体-主表 t_meta_personalscheme

- **表名称：** 个性化方案实体-主表
- **表名：** t_meta_personalscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmainschemedesign | 首页方案 （设计） | text | 0 |  |  | null | 首页方案 （设计） |
| 3 | fmainscheme | 首页方案 （运行期） | text | 0 |  |  | null | 首页方案 （运行期） |
| 4 | fwidgetcontainer | 首页小部件运行期内容 | text | 0 |  |  | null | 首页小部件运行期内容 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_personalscheme_pkey |  | fid |
| 2 | idx_kdp_personalscheme_num |  | fuserid |
