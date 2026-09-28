# 处理场景定义-pbd_scenedefine

## 处理场景定义-主表 t_pbd_scenedefine

- **表名称：** 处理场景定义-主表
- **表名：** t_pbd_scenedefine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 场景名称 | varchar | 512 |  | √ | ' ' | 场景名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fnumber | 场景编码 | varchar | 80 |  | √ | ' ' | 场景编码 |
| 8 | fentityid | 场景绑定实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_scenedefine_fnumber |  | fnumber |
| 2 | pk_pbd_scenedefine |  | fid |
