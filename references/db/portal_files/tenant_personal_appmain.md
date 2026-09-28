# 应用首页个性化方案实体-tenant_personal_appmain

## 应用首页个性化方案实体-主表 t_meta_appmainpersonal

- **表名称：** 应用首页个性化方案实体-主表
- **表名：** t_meta_appmainpersonal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fappmainschemedesign | 工作台设计期方案 | text | 0 |  |  | null | 工作台设计期方案 |
| 3 | fwidgetcontainer | 小部件运行期内容 | text | 0 |  |  | null | 小部件运行期内容 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户 |
| 5 | fappmainscheme | 工作台运行期方案 | text | 0 |  |  | null | 工作台运行期方案 |
| 6 | fappid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_appmainp_num |  | fuserid |
| 2 | t_meta_appmainpersonal_pkey |  | fid |
