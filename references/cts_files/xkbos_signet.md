# 状态印章配置-xkbos_signet

## 状态印章配置-主表 t_xkbas_signet

- **表名称：** 状态印章配置-主表
- **表名：** t_xkbas_signet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshow | 启用印章显示 | bpchar | 1 |  | √ | '1' | 启用印章显示 |
| 3 | flevel | 对象级别 | varchar | 10 |  | √ | ' ' | 对象级别,枚举: root :根节点 cloud :云节点 app :应用节点 object :业务对象节点 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fpictures | 图片设置隐藏域 | text | 0 |  |  | null | 图片设置隐藏域 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fobjectid | 对象编码 | varchar | 36 |  | √ | ' ' | 对象编码 |
| 9 | fmargintop | 上边距(PX) | int2 | 16 |  | √ | 0 | 上边距(PX) |
| 10 | fmarginleft | 左边距(PX) | int2 | 16 |  | √ | 0 | 左边距(PX) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbas_signet |  | fid |
| 2 | idx_xkbas_signet_fobjectid |  | fobjectid |
