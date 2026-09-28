# 用户首页卡片关联表-mpdm_usercardrelation

## 用户首页卡片关联表-主表 t_mpdm_userhcardrel

- **表名称：** 用户首页卡片关联表-主表
- **表名：** t_mpdm_userhcardrel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhomecardid | 首页卡片 | int8 | 64 |  | √ | 0 | [移动首页卡片 mpdm_homecardconfig](../mpdm_files/mpdm_homecardconfig.md) |
| 3 | fseqnumber | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 4 | fmobhomeschemeid | 移动首页方案 | int8 | 64 |  | √ | 0 | [移动首页方案 mpdm_hpschemeconfig](../mpdm_files/mpdm_hpschemeconfig.md) |
| 5 | fmobhomeappid | fmobhomeappid | int8 | 64 |  | √ | 0 |  |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisshow | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_userhcard_user |  | fuserid |
| 2 | pk_mpdm_userhcardrel |  | fid |
