# 基础数据操作验权组织关系-bd_entityoporgview

## 基础数据操作验权组织关系-主表 t_bd_entityoporgview

- **表名称：** 基础数据操作验权组织关系-主表
- **表名：** t_bd_entityoporgview

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbasedataid | 基础数据 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | foperation | 操作类型 | varchar | 20 |  | √ | ' ' | 操作类型,枚举: new :新增 modify :修改 view :查看 filter :过滤 draft :暂存 save :保存 submit :提交 audit :审核 unaudit :反审核 delete :删除 disable :禁用 enable :启用 close :关闭 copy :复制 assign :分配 unassign :取消分配 |
| 4 | forgproperty | 组织属性 | varchar | 20 |  | √ | ' ' | 组织属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_entityoporgview_pkey |  | fid |
| 2 | idx_entityoporgview_basedata |  | fbasedataid |
